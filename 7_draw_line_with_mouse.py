import numpy as np
import cv2


# Define mouse click callback function
def click_event(event, x, y, flags, param):
    # Left button down
    if event == cv2.EVENT_LBUTTONDOWN:
        # Draw a fill blue circle at the x/y location
        cv2.circle(img, (x, y), 3, (255, 0, 0), -1)

        # Append new point to points array
        points.append((x, y))

        # When more than 2 points are click, draw a line base from previous point to current point
        if len(points) >= 2:
            cv2.line(img, points[-2], points[-1], (255, 0, 0), 5)
        cv2.imshow('frame', img)

# Create a black color 512x512 BGR image
img = np.zeros((512, 512, 3), np.uint8)
cv2.imshow('frame', img)

# Initialize the points array
points = []

# Set mouse callback event to click_event function
cv2.setMouseCallback('frame', click_event)

# Wait for any keypress
cv2.waitKeyEx(0)

# Close all windows
cv2.destroyAllWindows()
