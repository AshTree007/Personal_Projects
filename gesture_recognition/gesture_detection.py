import torch
import torch.nn as nn
import pandas as pd
from sklearn.preprocessing import LabelEncoder

with torch.serialization.safe_globals([LabelEncoder]):
    le = torch.load("label_encoder.pth", weights_only=False)

model = nn.Sequential(
    nn.Linear(63, 128),
    nn.ReLU(),
    nn.Linear(128,64),
    nn.ReLU(),
    nn.Linear(64,32),
    nn.ReLU(),
    nn.Linear(32,16),
    nn.ReLU(),
    nn.Linear(16, 7)
)

model.load_state_dict(torch.load("model.pth"))
model.eval()

def predict(x):
    if len(x)==63:
        with torch.no_grad():
            output = model(torch.tensor(x).unsqueeze(0))
            probs = torch.softmax(output, dim=1)
            max_prob, pred_idx = torch.max(probs, dim=1)
            if max_prob.item() < .7: #sets threshold for "other"
                return "Other"
            return le.inverse_transform([pred_idx.item()])[0]
    return "failed prediction"
