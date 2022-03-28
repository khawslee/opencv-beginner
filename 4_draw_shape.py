# Import library
import numpy as np
import cv2

# Create black color BGR image with array of 512x512x3 fill with zero
img = np.zeros([512, 512, 3], np.uint8)

# Draw 10px thickness red color line start from (0,0) to (255,255)
img = cv2.line(img, (0, 0), (255, 255), (0, 0, 255), 10)

# Draw 10px thickness blue color arrow line start from (0,300) to (300,300)
img = cv2.arrowedLine(img, (0, 300), (300, 300), (255, 0, 0), 10)

# Draw 10px thickness red color rectangle start from (200,0) to (400,400)
img = cv2.rectangle(img, (200, 0), (400, 400), (0, 0, 255), 10)

# Draw 10px thickness green color circle start center at (400,100) with 63 radius
img = cv2.circle(img, (400, 100), 63, (0, 255, 0), 10)

# Set font
font = cv2.FONT_HERSHEY_COMPLEX
# Draw white color text, font size multiply of 2, thickness of 5
img = cv2.putText(img, 'Hello', (0, 400), font, 2, (255, 255, 255), 5)

# Show the image in new window
cv2.imshow('image', img)

# Waiting until key press
k = cv2.waitKey(0)

# If key press is ESC, close all windows
cv2.destroyAllWindows()
