import numpy as np
import cv2

# Create black color background image size 500 x 250
img1 = np.zeros((250, 500, 3), np.uint8)

# Create white rectangle top left y,x (200,0) to (300, 100) middle of image
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)

# Read blackwhite image
img2 = cv2.imread("./asset/blackwhite.jpg")

# Bitwise AND img2 and img1
bitAnd = cv2.bitwise_and(img2, img1)
# Bitwise OR img2 and img1
bitOr = cv2.bitwise_or(img2, img1)
# Bitwise XOR img2 and img1
bitXor = cv2.bitwise_xor(img2, img1)
# Bitwise NOT img1
bitNot1 = cv2.bitwise_not(img1)
# Bitwise NOT img2
bitNot2 = cv2.bitwise_not(img2)

# Show each operation in their respective windows
cv2.imshow("bitAnd", bitAnd)
cv2.imshow("bitOr", bitOr)
cv2.imshow("bitXor", bitXor)
cv2.imshow("bitNot1", bitNot1)
cv2.imshow("bitNot2", bitNot2)

# Wait for keypress
cv2.waitKeyEx(0)
# Close all windows
cv2.destroyAllWindows()