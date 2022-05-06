import cv2

# Read shapes.jpg in original mode
img = cv2.imread('./asset/shapes.jpg')
# Convert the image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Find threshold of image
_, thresh = cv2.threshold(imgGray, 240, 255, cv2.THRESH_BINARY)
# Find contour
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

# Foreach contour in contours
for contour in contours:
    # Approximate polygon shape with approximate accuracy
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    # Draw line on contour
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx);
        aspectRatio = float(w) / h
        if aspectRatio > 0.95 and aspectRatio <= 1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

# Show the image in new window
cv2.imshow('image', img)

# Waiting until key press
k = cv2.waitKey(0)

# If key press is ESC, close all windows
if k == 27:
    cv2.destroyAllWindows()
