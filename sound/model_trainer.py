import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import TensorDataset, DataLoader


data = []
labels = []

with open("output.csv", "r") as f:
    for line in f:
        nums = line.split(",")
        last = nums.pop(-1).strip()
        labels.append(ord(last)-64 if len(last)==1 else 0)
        data.append(nums)

data = np.array(data, np.float32)
X = torch.tensor(data, dtype=torch.float32)
y = torch.tensor(labels, dtype=torch.long)

dataset = TensorDataset(X, y)
loader = DataLoader(dataset, batch_size=32, shuffle=True)

model = nn.Sequential(
    nn.Linear(X.shape[1], 128),
    nn.ReLU(),
    nn.Linear(128,64),
    nn.ReLU(),
    nn.Linear(64,32),
    nn.ReLU(),
    nn.Linear(32,16),
    nn.ReLU(),
    nn.Linear(16, 27)
)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=.0001)

epochs = 5 
for epoch in range(epochs):
    for batch_X, batch_y in loader:
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.item():.4f}")


print("Training Done")

print("Evaluating...")

model.eval()

correct = 0
wrong = 0
with torch.no_grad():
    for i in range(len(X)):
        output = model(X[i].unsqueeze(0))  # Add batch dimension
        predicted = torch.argmax(output)    # Get predicted class
        if predicted.item() == y[i].item():
            correct += 1
        else:
            wrong += 1

print(f"Correct#: {correct}, wrong#: {wrong}")
print(f"Correct%: {correct/(correct+wrong)}")
print(X.shape[1])

save = input("Should it be saved? ").strip("\n")

while(save != "yes, save" and save != "no, don't save"):
    save = input("Should it be saved? ").strip("\n")

if save == "yes, save":
    torch.save(model.state_dict(), "model.pth")
    print("saved model")

else:
    print("didn't save")
