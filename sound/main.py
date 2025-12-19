import sounddevice as sd
from predictor import predict
import numpy as np
import noisereduce as nr

fs = int(sd.query_devices(kind="input")["default_samplerate"]/3) # sample rate
time = 1 # second

rec = sd.rec(frames=int(time*fs), samplerate= fs, channels= 1, dtype="float32")
print("speak")
sd.wait()
print("done")
rec = rec.flatten()
print("flattened")
#print(l)

reduced_noise = nr.reduce_noise(y=rec, sr=fs, stationary=True)
print("reduced")

sd.play(np.array(reduced_noise),fs)
sd.wait()

l = [float(x.item()) for x in reduced_noise]

print(predict(reduced_noise))