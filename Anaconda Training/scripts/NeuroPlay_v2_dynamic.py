import cv2
import random
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    focus_level = random.randint(50, 100)

    if focus_level < 65:
        color = (0, 0, 255)
    elif focus_level < 80:
        color = (0, 255, 255)
    else:
        color = (0, 255, 0)

    darkness = max(0, 80 - focus_level) / 100.0
    overlay = frame.copy()
    frame = cv2.addWeighted(overlay, 1 - darkness, np.zeros_like(frame), darkness, 0)

    cv2.putText(frame, f"Focus Level: {focus_level}%", (30, 60),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

    bar_width = int(focus_level * 5)
    cv2.rectangle(frame, (30, 100), (530, 130), (50, 50, 50), 2)
    cv2.rectangle(frame, (30, 100), (30 + bar_width, 130), color, -1)

    if focus_level < 60:
        cv2.putText(frame, "⚠️ Focus! Stay alert!", (300, 400),
                    cv2.FONT_HERSHEY_DUPLEX, 1.1, (0, 0, 255), 3)

    cv2.imshow("NeuroPlay Lite Pro v2 - Dynamic Focus", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
