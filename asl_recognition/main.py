import cv2
from img_processor import img_processor as improcess
import time

stream = cv2.VideoCapture(0)

if not stream:
    print("Couldn't capture stream")
    exit()

mode = "training"

count = total_rows = 0

data = []

if mode == "training":
    gesture = input("Enter the gesture you are training: ").lower()

while True:
    ret, frame = stream.read()

    frame, l = improcess(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))

    cv2.imshow("stream", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    if mode == "training":
        if l:
            data.extend(l)
            count += 1
        if count == 10:
            with open("data.csv", "a") as f:
                for thing in data:
                    f.write(",".join([str(x) for x in thing]))
                f.write(f", {gesture} \n")
            total_rows += 1
            print("wrote data")
            data = []
            count = 0
        if total_rows >= 1000:
            print("Collected 1000 rows, stopping.")
            break

    if cv2.waitKey(1) == ord('q'):
        print("Done")
        break

stream.release()
cv2.destroyAllWindows()