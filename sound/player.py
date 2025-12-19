import sounddevice as sd
import numpy as np

# Use a standard safe sample rate
fs = int(44100/3)

# Generate a 1-second 440 Hz tone at a safe amplitude (1D float32 array)
# t = np.linspace(0, 1, fs, endpoint=False)
# freq = 440.0
# arr = (0.1 * np.sin(2 * np.pi * freq * t)).astype("float32")

# Play and block until finished
# sd.play(arr, fs)
# sd.wait()

last_letter = ""
lens = []
with open("output.csv", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split(",")
        name = parts.pop(-1)
        # if name != last_letter:
        # Convert remaining parts to floats
        lens.append(len(parts))
        samples = [float(p) for p in parts]
        samples = np.array(samples, dtype="float32")
        print(name)
        #sd.play(samples, fs)
        #sd.wait()
        last_letter = name

print(lens)