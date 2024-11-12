
from flask import Flask, render_template, request
import pyrebase

app = Flask(__name__)




firebaseConfig = {
  "apiKey": "AIzaSyDVJFcGq6sbnHNycjBsBM0XB02v4ycLCJE",
  "authDomain": "weatherstation-32e7d.firebaseapp.com",
  "databaseURL": "https://weatherstation-32e7d-default-rtdb.firebaseio.com",
  "projectId": "weatherstation-32e7d",
  "storageBucket": "weatherstation-32e7d.appspot.com",
  "messagingSenderId": "471763717730",
  "appId": "1:471763717730:web:6c79d3b0b4aaf96993cb3b",
  "measurementId": "G-3L6VSHBXH8"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

@app.route('/', methods=['GET', 'POST'])
def home():
    location = "Ahmedabad"  # Default location is Ahmedabad

    if request.method == 'POST':
        # Get the location entered by the user
        location = request.form.get('location', 'Ahmedabad')

    # Search Firebase for weather data where location matches the input
    stations = db.get().val()  # Fetch all stations from Firebase
    weather = None

    # Search for the location in the stations data
    for station, data in stations.items():
        latest_data = list(data.values())[-1]  # Get the latest weather data entry
        if latest_data.get('location') and location.lower() in latest_data['location'].lower():
            weather = latest_data
            break

    return render_template('home.html', weather=weather, location=location)

@app.route('/history', methods=['GET', 'POST'])
def history():
    location = "Ahmedabad"  # Default to Ahmedabad weather history

    if request.method == 'POST':
        # Get the location entered by the user
        location = request.form.get('location', 'Ahmedabad')

    # Fetch weather data for the station that matches the location
    stations = db.get().val()  # Fetch all stations from Firebase
    weather_history = None

    # Search for the location in the stations data
    for station, data in stations.items():
        latest_data = list(data.values())[-1]
        if latest_data.get('location') and location.lower() in latest_data['location'].lower():
            weather_history = data
            break

    return render_template('history.html', history=weather_history, location=location)

@app.route('/errors')
def errors():
    # Fetch all errors from the Firebase database
    errors = db.child("Errors").get().val()

    return render_template('errors.html', errors=errors)

if __name__ == '__main__':
    app.run(debug=True)
