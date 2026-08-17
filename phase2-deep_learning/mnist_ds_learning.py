import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

# ---------------------------------------------------------------------------
# DATA: download MNIST. ToTensor() turns each 28x28 image into a tensor of
# shape (1, 28, 28) -- 1 channel (grayscale), 28 rows, 28 cols -- and scales
# pixel values from 0-255 down to 0.0-1.0 (networks train better on small numbers).
# ---------------------------------------------------------------------------
tf = transforms.ToTensor()
train_ds = datasets.MNIST(root="data", train=True,  download=True, transform=tf)
test_ds  = datasets.MNIST(root="data", train=False, download=True, transform=tf)

# DataLoader feeds the network data in BATCHES (64 images at a time) instead of
# one-by-one. Batching is faster and makes gradient descent more stable.
train_loader = DataLoader(train_ds, batch_size=64, shuffle=True)
test_loader  = DataLoader(test_ds,  batch_size=64)

# ---------------------------------------------------------------------------
# THE CNN
# ---------------------------------------------------------------------------
class DigitCNN(nn.Module):
    def __init__(self):
        super().__init__()
        # Conv2d(in_channels, out_channels, kernel_size, padding)
        #   in=1: input has 1 channel (grayscale)
        #   out=16: use 16 DIFFERENT learned kernels -> 16 feature maps
        #   kernel_size=3: each kernel is 3x3 (9 weights, shared across the image)
        #   padding=1: add a 1-pixel border so a 3x3 kernel keeps the size at 28x28
        self.conv1 = nn.Conv2d(1, 16, kernel_size=3, padding=1)
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, padding=1)  # 16 maps in, 32 out

        self.pool = nn.MaxPool2d(2)   # keep the max of each 2x2 block -> halves H and W
        self.relu = nn.ReLU()         # the non-linear bend, after each conv

        # After two conv+pool stages, each image is 32 channels of 7x7 (see below).
        # Flatten those into one long vector so a Linear classifier can read them.
        self.fc1 = nn.Linear(32 * 7 * 7, 64)   # 1568 numbers -> 64
        self.fc2 = nn.Linear(64, 10)           # 64 -> 10 class scores (one per digit)

    def forward(self, x):
        # x comes in as (batch, 1, 28, 28)
        x = self.pool(self.relu(self.conv1(x)))   # -> (batch, 16, 14, 14)
        x = self.pool(self.relu(self.conv2(x)))   # -> (batch, 32, 7, 7)
        x = x.flatten(1)                          # -> (batch, 1568)  flatten all but batch
        x = self.relu(self.fc1(x))                # -> (batch, 64)
        x = self.fc2(x)                           # -> (batch, 10)  raw scores ("logits")
        return x

device = "mps" if torch.backends.mps.is_available() else "cpu"  # M4 GPU if available
print(device+"- device")
net = DigitCNN().to(device)

# CrossEntropyLoss = the right loss for CLASSIFICATION (not MSE). It compares the
# 10 predicted scores against the true digit label. (More on why below.)
loss_fn = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001)

# ---------------------------------------------------------------------------
# TRAIN -- the same zero / backward / step heartbeat you already own
# ---------------------------------------------------------------------------
for epoch in range(3):                      # 3 passes over 60,000 images is plenty here
    net.train()
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        optimizer.zero_grad()               # (1) clear old gradients
        outputs = net(images)               #     forward pass -> (64, 10) scores
        loss = loss_fn(outputs, labels)     #     how wrong are the scores?
        loss.backward()                     # (2) autograd computes all gradients
        optimizer.step()                    # (3) nudge every weight downhill

    # --- check accuracy on the TEST set (images it never trained on) ---
    net.eval()
    correct = total = 0
    with torch.no_grad():                   # no gradients needed for evaluation
        for images, labels in test_loader:
            images, labels = images.to(device), labels.to(device)
            preds = net(images).argmax(1)   # pick the highest-scoring class per image
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    print(f"epoch {epoch+1} | test accuracy: {100*correct/total:.2f}%")
    import matplotlib.pyplot as plt

# conv1.weight holds the learned kernels: shape (16, 1, 3, 3)
# = 16 kernels, 1 input channel each, 3x3 spatial
kernels = net.conv1.weight.detach().cpu()   # detach: strip gradient tracking to view
print("kernel tensor shape:", kernels.shape)

fig, axes = plt.subplots(2, 8, figsize=(12, 3.5))
for i, ax in enumerate(axes.flat):
    k = kernels[i, 0]                        # the i-th kernel's 3x3 grid
    ax.imshow(k, cmap='gray')                # show its 9 weights as a tiny image
    ax.set_title(f"k{i}", fontsize=8)
    ax.axis('off')
plt.suptitle("conv1's 16 learned kernels (started as random noise)")
plt.tight_layout()
plt.show()

torch.save(net.state_dict(), "digit_cnn.pth")   # save all learned weights to a file
print("saved model weights to digit_cnn.pth")


import matplotlib.pyplot as plt
import torch

net = DigitCNN().to(device)                          # 1. build the SAME architecture (random weights)
net.load_state_dict(torch.load("digit_cnn.pth"))
net.eval()
wrong_images, wrong_pred, wrong_true = [], [], []

with torch.no_grad():
    for images, labels in test_loader:
        images_d = images.to(device)
        outputs = net(images_d)
        preds = outputs.argmax(1).cpu()
        print(preds)

        # find the indices in this batch where prediction != truth
        mismatch = (preds != labels).nonzero(as_tuple=True)[0]
        for idx in mismatch:
            wrong_images.append(images[idx])      # keep the image (on cpu)
            wrong_pred.append(preds[idx].item())
            wrong_true.append(labels[idx].item())

print(f"total misclassified: {len(wrong_images)} out of 10000")

# show the first 20 mistakes
fig, axes = plt.subplots(2, 10, figsize=(15, 3.5))
for i, ax in enumerate(axes.flat):
    ax.imshow(wrong_images[i].squeeze(), cmap='gray')   # squeeze: (1,28,28)->(28,28)
    ax.set_title(f"P:{wrong_pred[i]} T:{wrong_true[i]}", fontsize=9)
    ax.axis('off')
plt.suptitle("Where the network fails (P = predicted, T = true)")
plt.tight_layout()
plt.show()