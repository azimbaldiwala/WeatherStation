import RPi.GPIO as GPIO
import time

SENSOR_PIN = 17

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

def detect_rain():
    try:
        # Check the sensor input
        if GPIO.input(SENSOR_PIN):
            # No rain 
            return "NO" 
        else:
            # Rain
            return "YES"
    except:
        return "#Error"

if __name__ == "__main__":
    try:
        while True:
            rain_status = detect_rain()
            print(rain_status)
            time.sleep(1)

    except KeyboardInterrupt:
        print("Program stopped")

    finally:
        GPIO.cleanup()
