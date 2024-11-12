import dht11
import LDR_sensor as ldr 
import DetectRain
from time import sleep
from datetime import datetime
import firebase
import logDatabase
import analog_sensors
import configs


# Load Configs 
config = configs.load_config()
DEVICE_NAME = config["DEVICE_NAME"]
DEVICE_LOCATION = config["DEVICE_LOCATION"]


def getDateTime():
    now = datetime.now()
    # Format the date and time
    current_date = datetime.now().strftime("%d-%m-%y")
    current_time = datetime.now().strftime("%H:%M:%S")
    return current_date, current_time


# Every 30 secs send data to firebase 

def main():
    global DEVICE_NAME, DEVICE_LOCATION

    current_date, current_time = getDateTime()

    # Read data from the sensors 
    humidity, temperature = dht11.readTemperatureAndHumidity()
    rain = DetectRain.detect_rain()
    day_light = ldr.detect_light_intensity()

    analog_sensors_data = analog_sensors.read_sensors()

    
    rain = analog_sensors_data['Rain Sensor']
    air_quality = analog_sensors_data['MQ135']
    wind_speed = analog_sensors_data['Wind Speed']


    day_type = "to_be_implemented"
    

    

    weather_data = {
        "location": DEVICE_LOCATION,
        "date": current_date,
        "time": current_time,
        "temperature": str(temperature),
        "humidity": str(humidity),
        "day_type": day_type,
        "rain": str(rain),
        "day_light": str(day_light),
        "air_quality": air_quality,
        "wind_speed": wind_speed
    }

    print("Weather Data: ", weather_data)

    firebase_status = firebase.pushData(DEVICE_NAME, weather_data=weather_data)
    if firebase_status:
        firebase_status = "True"
    else: 
        firebase_status = "False"
        
    log_status = logDatabase.insert_log_entry(current_date, current_time, firebase_status, temperature, humidity, day_type, rain, day_light, air_quality)
    print(log_status)
    sleep(30)

if __name__ == "__main__":
    while True:
        main()
