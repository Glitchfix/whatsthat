import cv2

# Create a VideoCapture object to capture frames from the camera
cap = cv2.VideoCapture(0)
# cap.release()
# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open camera")
    exit()

# Function to capture and display a single frame from the camera
def capture_frame():
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was successfully read
    if not ret:
        print("Failed to read frame from camera")
        return

    # Display the frame
    cv2.imshow("Camera Stream", frame)
    return frame

# Call the capture_frame function to capture and display a single frame
capture_frame()


# Release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()