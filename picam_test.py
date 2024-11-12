from picamera import PiCamera
from time import sleep

# Initialize the camera
camera = PiCamera()

# Optionally, rotate the camera (0, 90, 180, 270)
camera.rotation = 0

# Start the camera preview
camera.start_preview()

# Wait for 2 seconds to allow the camera to adjust to lighting conditions
sleep(2)

# Capture an image
camera.capture('/home/pi/Desktop/image.jpg')

# Stop the camera preview
camera.stop_preview()

# Release the camera resources
camera.close()
