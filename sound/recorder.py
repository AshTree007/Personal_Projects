import sounddevice as sd
import numpy as np
import noisereduce as nr

fs = int(sd.query_devices(kind="input")["default_samplerate"]/3) # sample rate

num_inputs = 3#int(input("How many data points do you want to record: "))
thing_recorded = input("What do you want to record: ").upper()
time = 1 #seconds

times = 0

while times < num_inputs:
    print(f"start recording {times+1} now...")
    rec = sd.rec(frames=int(time*fs), samplerate= fs, channels= 1, dtype="float32")
    sd.wait()
    print("recording done...")

    rec = rec.flatten()
    rec = nr.reduce_noise(y=rec, sr=fs, stationary=True)

    with open("output.csv", "a") as f:
        np.savetxt(f, rec, newline=",")
        f.write(f"{thing_recorded}\n")

    print("\n\n\n\n\n\n")
    times+=1