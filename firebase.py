import pyrebase 
from datetime import datetime
import error_handler
import buzzer
import configs


#Load configs from config.txt
config = configs.load_config()


# Firebase Credentials 

firebaseConfig = {
    "apiKey": config['apiKey'],
    "authDomain": config['authDomain'],
    "projectId": config['projectId'],
    "storageBucket": config['storageBucket'],
    "messagingSenderId": config['messagingSenderId'],
    "appId": config['appId'],
    "measurementId": config['measurementId'],
    "databaseURL": config['databaseURL']
}


fierbase = pyrebase.initialize_app(firebaseConfig)
db = fierbase.database()
current_time = datetime.now().strftime("%H:%M:%S")


#weather data structure: 

weather_data = {
    "location": "AZIM,SKJ,AHM",
    "date": "04-08-24",
    "time": "22:14:00",
    "temperature": "26.0",
    "humidity": "85.0%",
    "day_type": "sunny",
    "rain": "Yes",
    "day_light": "Low",
    "air_quality": "poor",
    "wind_speed": "10 kmph"
}


def pushData(device_name, weather_data):
    global current_time
    try:
        db.child(device_name).push(weather_data)
        print(f"Data inserted at {current_time}: {weather_data}")
    except: 
        # returns custom error code 
        error_handler.log_error("Firebase Error!")
        # Sensor failed buzzer error code 3 beeps
        buzzer.beep_buzzer(0.5, 3)
        return False 
    return True 

def getData():
    pass


if __name__ == "__main__":
    # default device name...
    device_name = "ALFA17"
    status = pushData(device_name,weather_data)
    if status:
        print("Data Pushed!")
    else: 
        print("Error Pushing the data!")