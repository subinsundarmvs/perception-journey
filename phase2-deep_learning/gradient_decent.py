# Learn the hidden relationship y = 2x, WITHOUT being told the 2.

# Training data: examples of (x, true_y). The "2" is hidden in here.
data = [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]

w = 0.5          # the WEIGHT -- start with a random wrong guess
lr = 0.01        # the LEARNING RATE -- how big a step we take downhill

for epoch in range(50):          # 50 passes over the data
    total_loss = 0
    for x, true_y in data:
        pred = w * x                     # PREDICT with current weight
        error = pred - true_y            # how far off (signed)
        loss = error ** 2                # LOSS: squared error (always positive)
        total_loss += loss

        # GRADIENT of loss w.r.t. w:  d/dw (w*x - y)^2  =  2 * (w*x - y) * x
        grad = 2 * error * x

        # GRADIENT DESCENT: step w downhill (opposite the gradient)
        w = w - lr * grad

    # print(f"epoch {epoch:2d} | w = {w:.4f} |grad = {grad:.4f}| loss = {total_loss:.4f}")

# print(f"\nLearned w = {w:.4f}  (the hidden answer was 2)")


#  with pytorch 
import torch
# torch = PyTorch. Its core object is the "tensor": like a NumPy array, but with
# two superpowers -> (1) it can run on a GPU, (2) it can be tracked so PyTorch
# computes gradients through it automatically (this is "autograd").

# ---------------------------------------------------------------------------
# TRAINING DATA: examples of (x, true_y). The hidden rule is y = 2x, but we
# never tell the model the "2" -- it must DISCOVER it from these examples.
# ---------------------------------------------------------------------------
data = [(1.0, 2.0), (2.0, 4.0), (3.0, 6.0), (4.0, 8.0), (5.0, 10.0)]

# ---------------------------------------------------------------------------
# THE WEIGHT we want to learn. It's the single number the model adjusts.
#   torch.tensor(0.5)          -> wrap the number 0.5 as a tensor
#   requires_grad=True         -> "TRACK this tensor": PyTorch will record every
#                                 operation done with w, so it can later compute
#                                 d(loss)/dw automatically. This flag is what makes
#                                 w a *learnable* parameter rather than plain data.
# We start at 0.5 -- a deliberately WRONG guess. The right answer is 2.0.
# ---------------------------------------------------------------------------
w = torch.tensor(0.5, requires_grad=True)

lr = 0.01   # LEARNING RATE: how big a step we take downhill each update.
            # too small -> slow to converge; too big -> overshoots and diverges.

# ---------------------------------------------------------------------------
# TRAINING LOOP: repeat "predict -> measure error -> step downhill" many times.
# One "epoch" = one full pass over all the data.
# ---------------------------------------------------------------------------
for epoch in range(50):
    total_loss = 0.0

    for x, true_y in data:
        # Wrap this example's numbers as tensors so they can flow through the
        # same math as w. These are DATA, not parameters, so NO requires_grad --
        # we don't want gradients w.r.t. the inputs, only w.r.t. the weight w.
        x = torch.tensor(x)
        true_y = torch.tensor(true_y)

        # FORWARD PASS: make a prediction with the current weight.
        # Because w is tracked, PyTorch quietly RECORDS this multiply onto a
        # hidden "computation graph" so it can differentiate it later.
        pred = w * x

        # LOSS: a single number measuring how wrong this prediction is.
        # Squared error -> always positive, punishes big misses more.
        # This operation is ALSO recorded onto the graph.
        loss = (pred - true_y) ** 2

        # BACKWARD PASS (the magic): walk the recorded graph backwards and
        # compute the gradient of loss w.r.t. every tracked tensor (here, w).
        # After this call, w.grad holds d(loss)/dw -- the SLOPE that tells us
        # which way, and how steeply, to nudge w to reduce the loss.
        # We did this by hand before (2*error*x); autograd now does it for us.
        loss.backward()

        # .item() pulls the plain Python number OUT of a 1-element tensor,
        # just so we can add it up for printing.
        total_loss += loss.item()

        # WEIGHT UPDATE (gradient descent step). We must do this WITHOUT letting
        # PyTorch record it, because updating w is bookkeeping, not part of the
        # model's math. torch.no_grad() = "don't track anything in this block."
        with torch.no_grad():
            w -= lr * w.grad        # step w downhill: subtract (rate * slope)

        # RESET THE GRADIENT. PyTorch ACCUMULATES gradients -- each .backward()
        # ADDS to w.grad instead of replacing it. If we don't clear it, gradients
        # from previous steps pile up and corrupt training. This is the #1
        # beginner bug, so we zero it every iteration.
        w.grad.zero_()

    # Watch w climb from 0.5 toward 2.0, and loss shrink toward 0, each epoch.
    # print(f"epoch {epoch:2d} | w = {w.item():.4f} | loss = {total_loss:.4f}")

# By now w should sit very close to 2.0 -- the model DISCOVERED the hidden rule,
# using a gradient it computed automatically rather than one we derived by hand.
# print(f"\nLearned w = {w.item():.4f}  (autograd found the gradient, not me)")

#  Proper Code Flow

import torch

data = [(1.0, 2.0), (2.0, 4.0), (3.0, 6.0), (4.0, 8.0), (5.0, 10.0)]

w = torch.tensor(0.5, requires_grad=True)

# THE OPTIMIZER: give it the list of parameters to update and the learning rate.
# SGD = Stochastic Gradient Descent -- literally the "step downhill" rule you know.
# It now OWNS the update logic, so you never write w -= lr*grad or no_grad() again.
optimizer = torch.optim.SGD([w], lr=0.01)

for epoch in range(50):
    total_loss = 0.0
    for x, true_y in data:
        x = torch.tensor(x)
        true_y = torch.tensor(true_y)

        pred = w * x
        loss = (pred - true_y) ** 2

        optimizer.zero_grad()   # (1) clear old gradients -- replaces w.grad.zero_()
        loss.backward()         # (2) autograd computes the gradient (unchanged)
        optimizer.step()        # (3) update ALL params using their gradients --
                                #     replaces the no_grad() manual update

        total_loss += loss.item()

    print(f"epoch {epoch:2d} | w = {w.item():.4f} | loss = {total_loss:.4f}")

print(f"\nLearned w = {w.item():.4f}")