import numpy as np
import cv2


# Define mouse click callback function
def click_event(event, x, y, flags, param):
    # Left button down
    if event == cv2.EVENT_LBUTTONDOWN:
        # Print x/y coordinate on screen
        font = cv2.FONT_HERSHEY_SIMPLEX
        xy_string = str(x) + ', ' + str(y)
        cv2.putText(img, xy_string, (x, y), font, 0.5, (255, 255, 0), 2)
        cv2.imshow('frame', img)

    # Right button down
    if event == cv2.EVENT_RBUTTONDOWN:
        # Print BGR color on screen
        blue = img[y, x, 0]  # Blue is channel 0
        green = img[y, x, 1]  # Green is channel 1
        red = img[y, x, 2]  # Red is channel 2
        font = cv2.FONT_HERSHEY_SIMPLEX
        bgr_string = str(blue) + ', ' + str(green) + ', ' + str(red)
        cv2.putText(img, bgr_string, (x, y), font, 0.5, (0, 255, 255), 2)
        cv2.imshow('frame', img)


# Load demo image
img = cv2.imread('./asset/tennis.jpg')

# Show the image
cv2.imshow('frame', img)

# Set mouse callback event to click_event function
cv2.setMouseCallback('frame', click_event)

# Wait for any keypress
cv2.waitKeyEx(0)

# Close all windows
cv2.destroyAllWindows()
