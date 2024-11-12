import sqlite3


def insert_log_entry(date, time, data_send_to_firebase, temperature, humidity, day_type, rain_check, day_light, air_quality):
    try: 
        # Connect to the SQLite database
        conn = sqlite3.connect('weather_logs.db')
        cursor = conn.cursor()

        # Insert the data into the log_db table
        cursor.execute('''
        INSERT INTO log_db (date, time, data_send_to_firebase, temperature, humidity, day_type, rain_check, day_light, air_quality)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (date, time, data_send_to_firebase, temperature, humidity, day_type, rain_check, day_light, air_quality))

        # Commit the changes and close the connection
        conn.commit()
        conn.close()
        return "[+]LOG ENTRY MADE!"

    except:
        return "[-]LOG ENTRY FAILED!"


if __name__ == "__main__":
    insert_log_entry("04-08-24", "22:14:00", True, "26.0", "85.0%", "sunny", "Yes", "Low", "Sensor_not_connected")
