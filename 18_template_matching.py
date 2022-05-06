import cv2
import numpy as np

# Read image file
img = cv2.imread('ronaldo.jpg')
# Convert img to grayscale
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Read template image
template = cv2.imread('ball.jpg', 0)
# Define the width and height of template image
w, h = template.shape[::-1]

# Match template using template
res = cv2.matchTemplate(grey_img, template, cv2.TM_CCOEFF_NORMED)
# Define Threshold value
threshold = 0.80
# Return array where threshold above defined value
loc = np.where(res >= threshold)

# Draw red rectangle on the match object
for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2 )

# Show image with matching rectangle
cv2.imshow("image", img)
# Wait
cv2.waitKey(0)
# Destroy windows and release capture
cv2.destroyAllWindows()
