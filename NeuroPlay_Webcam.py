import cv2

# Open the default camera (0 = built-in camera, 1 = external)https://github.com/xzerite/Software-Engineering-/blob/main/camera_test
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Failed to open the camera.")
    exit()

print("✅ Camera started successfully. Press 'Q' to quit.")

while True:
    # Read each frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("⚠️ Failed to capture frame.")
        break

    # Display the live video feed
    cv2.imshow("Player Webcam", frame)

    # Press 'Q' to exit the webcam window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("🛑 Exiting the camera...")
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()


