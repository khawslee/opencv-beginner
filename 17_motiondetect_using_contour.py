import cv2

# Open video file
cap = cv2.VideoCapture('video_1.mp4')

# Read 1st frame of video into frame 1 and 2
ret, frame1 = cap.read()
ret, frame2 = cap.read()

while cap.isOpened():
    # Find the different between frame1 and frame2
    diff = cv2.absdiff(frame1, frame2)
    # Convert the diff into grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur on the different
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # Find the threshold
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # Dilate the threshold
    dilated = cv2.dilate(thresh, None, iterations=3)
    # Find the contours
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # foreach contours draw a rectangle area over the contour
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour)
        if cv2.contourArea(contour) < 600:
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("moved", frame1)

    # Copy frame2 to frame1
    frame1 = frame2
    # Read next frame from video into frame2
    ret, frame2 = cap.read()

    # Wait for ESC key
    if cv2.waitKey(40) == 27:
        break

# Destroy windows and release capture
cv2.destroyAllWindows()
cap.release()
