import serial
import time
import error_handler
import buzzer
import configs

config = configs.load_config()

SERIAL_PORT=config['SERIAL_PORT']
BAUD_RATE=int(config['BAUD_RATE'])
TIME_OUT=int(config['TIME_OUT'])

def read_sensors(serial_port=SERIAL_PORT, baud_rate=BAUD_RATE, timeout=1):
    """
    Reads data from the Arduino Nano over serial communication.

    Parameters:
    serial_port (str): The serial port to use for communication.
    baud_rate (int): The baud rate for serial communication.
    timeout (int): The timeout for serial communication.

    Returns:
    dict: A dictionary containing MQ135, rain sensor values, and wind speed.
    """
    ser = serial.Serial(serial_port, baud_rate, timeout=timeout)
    ser.flush()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            if "MQ135" in line and "Rain Sensor" in line and "Wind Speed" in line:
                try:
                    parts = line.split(", ")
                    mq135_value = int(parts[0].split(": ")[1])
                    rain_percentage = float(parts[1].split(": ")[1].replace("%", ""))
                    wind_speed = float(parts[2].split(": ")[1].replace(" km/h", ""))
                    return {"MQ135": mq135_value, "Rain Sensor": rain_percentage, "Wind Speed": wind_speed}
                except (IndexError, ValueError) as e:
                    # returns custom error code 
                    error_handler.log_error("DHT11 Sensor Failed!")
                    # Sensor failed buzzer error code 3 beeps
                    buzzer.beep_buzzer(0.5, 5)
                    print(f"Error parsing line: {e}")
                    continue
                
        time.sleep(1)

if __name__ == "__main__":
    sensor_data = read_sensors()
    print(f"MQ135 Value: {sensor_data['MQ135']}")
    print(f"Rain Sensor Percentage: {sensor_data['Rain Sensor']}%")
    print(f"Wind Speed: {sensor_data['Wind Speed']} km/h")
