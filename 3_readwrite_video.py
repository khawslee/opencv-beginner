import cv2

# Define a video capture object
cap = cv2.VideoCapture(0)

# Define output video as XVID, 20 frame and 640x480 size
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video_out.mp4', fourcc, 20.0, (640,480))

while cap.isOpened():
    # Capture the video frame by frame
    ret, frame = cap.read()

    if ret:
        # Output the frame to video writer
        out.write(frame)

        # Show the video in window
        cv2.imshow('Capture video', frame)

        # Wait for keypress 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release video capture object
cap.release()
# Release video writer object
out.release()
# Close all windows
cv2.destroyAllWindows()
