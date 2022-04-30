import numpy as np
import cv2

# Trackbar callback function
def trackbarCallback(x):
    print(x)


# Create black color background image size 512 x 300
img = np.zeros((300, 512, 3), np.uint8)

# Create a placeholder window for component
cv2.namedWindow('image')

# Create trackbar for color B, start 0 max 255.
cv2.createTrackbar('B', 'image', 0, 255, trackbarCallback)
# Create trackbar for color G, start 0 max 255.
cv2.createTrackbar('G', 'image', 0, 255, trackbarCallback)
# Create trackbar for color R, start 0 max 255.
cv2.createTrackbar('R', 'image', 0, 255, trackbarCallback)

# Continue to update image until ESC key press
while 1:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Get each trackbar position
    color_b = cv2.getTrackbarPos('B', 'image')
    color_g = cv2.getTrackbarPos('G', 'image')
    color_r = cv2.getTrackbarPos('R', 'image')

    # Replace the color of image with value from trackbar
    img[:] = [color_b, color_g, color_r]

# Close all windows
cv2.destroyAllWindows()
