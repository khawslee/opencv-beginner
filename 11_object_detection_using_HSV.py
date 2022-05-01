import numpy as np
import cv2


# Trackbar callback function
def trackbarCallback(x):
    pass

# Uncomment below to use video capture frame as input
cap = cv2.VideoCapture(0)

# Create a placeholder window for component
cv2.namedWindow("Tracking")

# Create trackbar for lower HSV and upper HSV
cv2.createTrackbar("LH", "Tracking", 0, 255, trackbarCallback)
cv2.createTrackbar("LS", "Tracking", 0, 255, trackbarCallback)
cv2.createTrackbar("LV", "Tracking", 0, 255, trackbarCallback)
cv2.createTrackbar("UH", "Tracking", 255, 255, trackbarCallback)
cv2.createTrackbar("US", "Tracking", 255, 255, trackbarCallback)
cv2.createTrackbar("UV", "Tracking", 255, 255, trackbarCallback)

# Continue to update image until ESC key press
while 1:
    # Open smarties image
    # frame = cv2.imread('smarties.png')
    # Uncomment below to use video capture frame as input, and comment the imread function
    _, frame = cap.read()

    # Convert the image color to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get each trackbar position
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    # Create lower HSV and upper HSV array
    lower_hsv = np.array([l_h, l_s, l_v])
    upper_hsv = np.array([u_h, u_s, u_v])

    # Create masking base on the lower HSV and upper HSV array
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

    # Bitwise AND both frame with masking
    res = cv2.bitwise_and(frame, frame, mask=mask)

    # Show all the windows
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    # Wait for ESC key press
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# Close all windows
cv2.destroyAllWindows()

# Below are the value of Lower and Upper HSV to mask BLUE and GREEN ball
# (81, 133, 0) (147, 255, 255) Blue
# (26, 223, 0) (111, 255, 255) Green
