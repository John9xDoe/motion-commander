import cv2
import mediapipe as mp
import pickle

import numpy as np

model_dict = pickle.load(open('./model.p', 'rb'))
model = model_dict['model']

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(min_detection_confidence=0.5, max_num_hands=1, static_image_mode=True)

cap = cv2.VideoCapture(0)


while True:
    data_aux = []
    x_ = []
    y_ = []

    ret, frame = cap.read()
    H, W, _ = frame.shape

    frame_rgb = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
            )

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                data_aux.append(x)
                data_aux.append(y)

                x_.append(x)
                y_.append(y)

        x1, y1 = int(min(x_) * W), int(min(y_) * H)
        x2, y2 = int(max(x_) * W), int(max(y_) * H)


        try:
            prediction = model.predict([np.asarray(data_aux)])
            cv2.putText(frame, str(prediction), (x1 - 10, y1 - 20), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 1, cv2.LINE_AA)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
            print(prediction)

        except:
            continue


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('frame', frame)

cap.release()
cv2.destroyAllWindows()
