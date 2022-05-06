import cv2

# Read demo.jpg in original mode
img = cv2.imread('./asset/demo.jpg', -1)

# Show the image in new window
cv2.imshow('image', img)

# Waiting until key press
k = cv2.waitKey(0)

# If key press is ESC, close all windows
if k == 27:
    cv2.destroyAllWindows()
# Else if key is 's', write the image to a new file then close all windows
elif k == ord('s'):
    cv2.imwrite('demo_copy.jpg', img)
    cv2.destroyAllWindows()
