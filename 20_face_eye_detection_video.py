import cv2

# Load Cascade Classifier configuration files
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Open video file
cap = cv2.VideoCapture('./asset/obama.mp4')

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break
    # Read face image and convert it to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect face using grayscale image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5, 0, [30, 30])
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 4)
    # Show the detection
    cv2.imshow("image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release capture
cap.release()
# Destroy windows and release capture
cv2.destroyAllWindows()