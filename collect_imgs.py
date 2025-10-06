import os
import cv2

DATA_DIR = './data'

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

classes = [
    'mouse_up',
    'mouse_down',
    'mouse_right',
    'mouse_left'
]
number_of_classes = 4
datasize = 250

cap = cv2.VideoCapture(0)

for cls in classes:
    if not os.path.exists(os.path.join(DATA_DIR, cls)):
        os.makedirs(os.path.join(DATA_DIR, str(cls)))

    print(f'Collecting data for class {cls}')

    done = False

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, 'Ready? Press "Q"', (200, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 1, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        if cv2.waitKey(25) == ord('q'):
            break

    cnt = 0

    while cnt < datasize:
        ret, frame = cap.read()
        cv2.imshow(f'class {cls}', frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(DATA_DIR, cls, '{}.jpg'.format(cnt)), frame)

        cnt += 1

cap.release()
cv2.destroyAllWindows()
