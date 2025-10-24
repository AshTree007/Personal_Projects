import mediapipe as mp
import gesture_detection as gd

mp_hands = mp.solutions.hands
hand = mp_hands.Hands()
mp_drawing = mp.solutions.drawing_utils

def img_processor(rgb_frame):

    result = hand.process(rgb_frame)

    landmark_list = []
    gesture = "None"

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            hand_coords = []
            for lm in hand_landmarks.landmark:
                hand_coords.extend([lm.x, lm.y, lm.z])
            landmark_list.append(hand_coords)
            mp_drawing.draw_landmarks(rgb_frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    if landmark_list:  
        gesture = gd.predict(landmark_list[0])
    return rgb_frame, gesture