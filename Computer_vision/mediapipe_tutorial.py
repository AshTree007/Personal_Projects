import mediapipe as mp
import cv2
import time
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

model_path = "model.task"

base_options = python.BaseOptions(model_asset_path = model_path)

Base_Options = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode

# Create a gesture recognizer instance with the live stream mode:
def print_result(result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int):
    try:
        with open("output", "r") as file:
            lines = file.readlines()
            last_gesture = lines[-1].strip() if lines else None
    except:
        last_gesture = None
   
        
    if result.gestures:
        gesture = result.gestures[0][0].category_name
        if gesture != "None" and gesture != last_gesture:
            with open("output", "a") as file:
                file.write(f"{gesture}\n")

options = GestureRecognizerOptions(
    base_options=python.BaseOptions(model_asset_path=model_path),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result,
    num_hands = 2,
    min_hand_detection_confidence = .75,
    min_hand_presence_confidence = .75)

with GestureRecognizer.create_from_options(options) as recognizer:
    stream = cv2.VideoCapture(0)

    if not stream.isOpened():
        print("No Stream")
    
    while True:
        ret, frame = stream.read()
        if not ret:
            print("Error in capturing Stream")
            break
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data = rgb_frame)
        recognizer.recognize_async(mp_image, time.clock_gettime_ns(time.CLOCK_MONOTONIC)//1000000)
        cv2.imshow("Hand Stuff", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    stream.release()
    cv2.destroyAllWindows()
    with open("output", "a") as file:
        file.write("--------End of Trial--------\n")