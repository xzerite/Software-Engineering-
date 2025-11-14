from flask import Flask, render_template, Response
import cv2
import random

app = Flask(__name__)

cap = cv2.VideoCapture(0)

rect_x = 50
rect_y = 200
rect_width = 100
rect_height = 50

def gen_frames():
    global rect_x
    while True:
        success, frame = cap.read()
        if not success:
            break

        focus_level = random.randint(50, 100)
        color = (0, 255, 0) if focus_level > 80 else (0, 255, 255) if focus_level > 65 else (0, 0, 255)

        cv2.putText(frame, f"Focus: {focus_level}%", (30, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        bar_width = int(focus_level * 5)
        cv2.rectangle(frame, (30, 100), (530, 130), (50, 50, 50), 2)
        cv2.rectangle(frame, (30, 100), (30 + bar_width, 130), color, -1)

        speed = 10 if focus_level > 80 else 6 if focus_level > 65 else 3
        rect_x += speed
        if rect_x > frame.shape[1]:
            rect_x = 0
        cv2.rectangle(frame, (rect_x, rect_y),
                      (rect_x + rect_width, rect_y + rect_height),
                      (255, 0, 0), -1)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
