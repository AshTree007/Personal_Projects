import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import TensorDataset, DataLoader

data = pd.read_csv("training_data.csv")
data = data.sample(frac=1, random_state=42).reset_index(drop=True)
X = torch.tensor(data.drop("label", axis=1).values, dtype=torch.float32)

le = LabelEncoder()
y = torch.tensor(le.fit_transform(data["label"]), dtype=torch.long)

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
    nn.Linear(16, 8)
)

criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=.0001)

epochs = 5000 
for epoch in range(epochs):
    for batch_X, batch_y in loader:
        outputs = model(batch_X)
        loss = criterion(outputs, batch_y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    print(f"Epoch {epoch+1}/{epochs} - Loss: {loss.item():.4f}")

torch.save(model.state_dict(), "model.pth")
torch.save(le, "label_encoder.pth")
print("All Done")

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
