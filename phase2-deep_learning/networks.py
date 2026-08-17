import torch
import torch.nn as nn
import matplotlib.pyplot as plt

# ---- data: the parabola a straight line cannot fit ----
x = torch.linspace(-3, 3, 100).reshape(-1, 1)   # 100 points, shape (100,1) for nn.Linear
y = x ** 2

# ---- a network we can peek inside ----
class SmallNet(nn.Module):
    def __init__(self, use_relu=True):
        super().__init__()
        self.layer1 = nn.Linear(1, 8)
        self.layer2 = nn.Linear(8, 1)
        self.relu = nn.ReLU()
        self.use_relu = use_relu

    def hidden(self, x):                 # <-- expose the 8 neuron outputs
        h = self.layer1(x)
        return self.relu(h) if self.use_relu else h

    def forward(self, x):
        return self.layer2(self.hidden(x))

def train(net, epochs=2000):
    opt = torch.optim.Adam(net.parameters(), lr=0.05)   # Adam = faster-converging SGD
    loss_fn = nn.MSELoss()
    for _ in range(epochs):
        opt.zero_grad()
        loss = loss_fn(net(x), y)
        loss.backward()
        opt.step()
    return loss.item()

net_relu = SmallNet(use_relu=True);  loss_relu = train(net_relu)
net_lin  = SmallNet(use_relu=False); loss_lin  = train(net_lin)
print(f"final loss WITH relu:    {loss_relu:.3f}")
print(f"final loss WITHOUT relu: {loss_lin:.3f}")

# ---- plots ----
xn = x.detach().numpy().ravel(); yn = y.detach().numpy().ravel()

fig, ax = plt.subplots(1, 3, figsize=(15, 4))

# 1) the 8 hidden neurons = 8 bent lines ("hockey sticks")
with torch.no_grad():
    hs = net_relu.hidden(x).numpy()
for i in range(8):
    ax[0].plot(xn, hs[:, i])
ax[0].set_title("the 8 hidden neurons (ReLU-bent lines)")

# 2) final fit vs truth, WITH relu
with torch.no_grad():
    ax[1].plot(xn, yn, 'k--', label='true x²')
    ax[1].plot(xn, net_relu(x).numpy().ravel(), 'r', label='network')
ax[1].legend(); ax[1].set_title(f"WITH ReLU (loss {loss_relu:.2f})")

# 3) WITHOUT relu -> can only draw a straight line, fails
with torch.no_grad():
    ax[2].plot(xn, yn, 'k--', label='true x²')
    ax[2].plot(xn, net_lin(x).numpy().ravel(), 'b', label='network (no ReLU)')
ax[2].legend(); ax[2].set_title(f"WITHOUT ReLU (loss {loss_lin:.2f})")

plt.tight_layout(); plt.show()