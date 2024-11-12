import pyrebase 
import datetime


# Firebase Credentials 

firebaseConfig = {
  "apiKey": "AIzaSyDVJFcGq6sbnHNycjBsBM0XB02v4ycLCJE",
  "authDomain": "weatherstation-32e7d.firebaseapp.com",
  "projectId": "weatherstation-32e7d",
  "storageBucket": "weatherstation-32e7d.appspot.com",
  "messagingSenderId": "471763717730",
  "appId": "1:471763717730:web:6c79d3b0b4aaf96993cb3b",
  "measurementId": "G-3L6VSHBXH8",
  "databaseURL": "https://weatherstation-32e7d-default-rtdb.firebaseio.com/"
}


# Initialize Pyrebase
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()


def log_error(error_message):
    # Get the current time and date
    now = datetime.datetime.now()
    error_time = now.strftime("%H:%M:%S")
    error_date = now.strftime("%Y-%m-%d")
    
    # Define the error data structure
    error_data = {
        'error_time': error_time,
        'error_date': error_date,
        'error_message': error_message
    }
    
    # Push the error data to the database
    db.child('Errors').push(error_data)
    
    print("Error logged to Firebase.")

if __name__ == "__main__":
    log_error("Sample Error!")


