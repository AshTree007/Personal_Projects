import cv2
import hand_detection as dt

stream = cv2.VideoCapture(0)

if not stream:
    print("couldn't caputre stream :(")
    exit()

while True:
    ret, frame = stream.read()

    if not ret:
        print("Couldn't read")
        break

    #### Hand detection part####
    frame, gesture = dt.img_processor(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    ####
    print(gesture)
    cv2.imshow("stream", cv2.flip(frame,1))
    if cv2.waitKey(1) == ord("q"):
        print("done")
        break

stream.release()
cv2.destroyAllWindows()