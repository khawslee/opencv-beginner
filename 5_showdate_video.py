import cv2
import datetime
# Define a video capture object
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # Capture the video frame by frame
    ret, frame = cap.read()

    if ret:
        # Set the font
        font = cv2.FONT_HERSHEY_SIMPLEX

        # Print the width and height of video on (10,25)
        text = 'Width: ' + str(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) + ' Height: ' + str(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cv2.putText(frame, text, (10, 25), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        # Print the date time on (10,60)
        datetext = 'Date: ' + str(datetime.datetime.now())
        cv2.putText(frame, datetext, (10, 60), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
        
        # Show the video in window
        cv2.imshow('Video', frame)

        # Wait for keypress 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release video capture object
cap.release()
# Close all windows
cv2.destroyAllWindows()
