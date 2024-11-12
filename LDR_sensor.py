import RPi.GPIO as GPIO
import time
import configs 
# GPIO pin where the digital output is connected

config = configs.load_config()


SENSOR_PIN = int(config['LDR_SENSOR'])

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

# Thresholds for light detection
high_threshold = 10  # Number of continuous reads to determine 'High'
medium_threshold = 5  # Number of continuous reads to determine 'Medium'
low_threshold = 2  # Number of continuous reads to determine 'Low'

def detect_light_intensity():

    try:
        high_count = 0
        medium_count = 0
        low_count = 0
        
        # Run a small loop to determine the light intensity
        for _ in range(15):  # Adjust the range as needed to get a stable reading
            if not GPIO.input(SENSOR_PIN):  # Inverting the input logic
                high_count += 1
                medium_count = max(0, medium_count - 1)
                low_count = max(0, low_count - 1)
            else:
                low_count += 1
                medium_count = max(0, medium_count - 1)
                high_count = max(0, high_count - 1)

            time.sleep(0.1)  # Adjust the sleep time as needed

        # Determine the intensity based on the counts
        if high_count >= high_threshold:
            return "High"
        elif medium_count >= medium_threshold:
            return "Medium"
        elif low_count >= low_threshold:
            return "Low"
        else:
            return "#Error"
    except:
        print("Error in LDR sensor!")
        
if __name__ == "__main__":
    try:
        intensity = detect_light_intensity()
        print(f"Light Intensity: {intensity}")

    except KeyboardInterrupt:
        print("Program stopped")

    finally:
        GPIO.cleanup()
