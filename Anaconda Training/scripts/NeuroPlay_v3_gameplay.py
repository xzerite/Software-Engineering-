import cv2
import random
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

rect_x = 50
rect_y = 200
rect_width = 100
rect_height = 50
speed = 5

while True:
    ret, frame = cap.read()
    if not ret:
        break

    focus_level = random.randint(50, 100)

    if focus_level > 80:
        speed = 15
    elif focus_level > 65:
        speed = 8
    else:
        speed = 3

    rect_x += speed
    if rect_x > frame.shape[1]:
        rect_x = 0

    cv2.rectangle(frame, (rect_x, rect_y),
                  (rect_x + rect_width, rect_y + rect_height),
                  (255, 0, 0), -1)

    bar_width = int(focus_level * 5)
    color = (0, 255, 0) if focus_level > 80 else (0, 255, 255) if focus_level > 65 else (0, 0, 255)
    cv2.rectangle(frame, (30, 100), (530, 130), (50, 50, 50), 2)
    cv2.rectangle(frame, (30, 100), (30 + bar_width, 130), color, -1)
    cv2.putText(frame, f"Focus: {focus_level}%", (30, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    if focus_level < 60:
        cv2.putText(frame, "⚠️ Focus! Stay alert!", (300, 400),
                    cv2.FONT_HERSHEY_DUPLEX, 1.1, (0, 0, 255), 3)

    cv2.imshow("NeuroPlay Lite Pro v3 - Gameplay Response", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
