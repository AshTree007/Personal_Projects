import torch
import torch.nn as nn
from sklearn.preprocessing import LabelEncoder


model = nn.Sequential(
    nn.Linear(14700, 128),
    nn.ReLU(),
    nn.Linear(128,64),
    nn.ReLU(),
    nn.Linear(64,32),
    nn.ReLU(),
    nn.Linear(32,16),
    nn.ReLU(),
    nn.Linear(16, 27)
)

model.load_state_dict(torch.load("model.pth"))
model.eval()

def predict(x):
    with torch.no_grad():
        output = model(torch.tensor(x).unsqueeze(0))
        probs = torch.softmax(output, dim=1)
        max_prob, pred_idx = torch.max(probs, dim=1)
        print(max_prob.item())
        if max_prob.item() < .7:
            return "FAILED"
        output = pred_idx.item()
        return chr(output+64) if output != 0 else "SILENCE"
    

if __name__ == "__main__":
    with open("output.csv", "r") as f:
        for line in f:
            l = line.split(",")
            l.pop(-1)
            l = [float(x) for x in l]
            print(predict(l))