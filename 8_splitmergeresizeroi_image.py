import numpy as np
import cv2

# Read demo.jpg in original mode
img = cv2.imread('./asset/tennis.jpg')
img2 = cv2.imread('./asset/opencv-logo.png')

# Split image into 3 color channel
b, g, r = cv2.split(img)

# Merge all color channel into image
img = cv2.merge((b, g, r))

# Slice the ball from image[y(size), x(size)]
ball = img[55:135, 278:358]

# Place the ball into image[y(size), x(size)]
img[73:153, 57:137] = ball

# Resize img to 600x600
img = cv2.resize(img, (600, 600))

# Resize img2 to 600x600
img2 = cv2.resize(img2, (600, 600))

# Add two image with opacity weight of 0.5 for img and 0.5 for img2
weightedImg = cv2.addWeighted(img, .5, img2, .5, 0)

# Show the weighted image in new window
cv2.imshow('image', weightedImg)

# Waiting until key press
k = cv2.waitKey(0)

# If key press, close all windows
cv2.destroyAllWindows()
