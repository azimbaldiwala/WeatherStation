import RPi.GPIO as GPIO
import time

def control_buzzer(duration):
    # Set the GPIO mode
    GPIO.setmode(GPIO.BCM)

    # Define the GPIO pin for the buzzer
    buzzer_pin = 22

    # Set up the buzzer pin as an output
    GPIO.setup(buzzer_pin, GPIO.OUT)

    try:
        # Turn the buzzer on
        GPIO.output(buzzer_pin, GPIO.HIGH)
        print("Buzzer on")
        
        # Wait for the specified duration
        time.sleep(duration)
        
        # Turn the buzzer off
        GPIO.output(buzzer_pin, GPIO.LOW)
        print("Buzzer off")
    
    finally:
        # Clean up the GPIO settings
        GPIO.cleanup()



def beep_buzzer(duration, times):
    for i in range(times):
        control_buzzer(duration)
