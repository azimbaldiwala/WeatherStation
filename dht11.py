import Adafruit_DHT
import error_handler
import buzzer
import configs

# Set sensor type and GPIO pin
sensor = Adafruit_DHT.DHT11

# Load config from config file 
DHT11_PIN = int(configs.load_config()['DHT11_PIN'])

gpio_pin = DHT11_PIN


def readTemperatureAndHumidity():
    global sensor, gpio_pin
    try: 
        humidity, temperature = Adafruit_DHT.read(sensor, gpio_pin)
        # return comma seperated value --> temp, humidity 
        return humidity, temperature 
    except:
        print("[+] Error while reading the Temperature and Humidity!")
        # returns custom error code 
        error_handler.log_error("DHT11 Sensor Failed!")
        # Sensor failed buzzer error code 5 beeps
        buzzer.beep_buzzer(0.5, 5)
        return "#Error"


if __name__ == "__main__":
    readTemperatureAndHumidity()
