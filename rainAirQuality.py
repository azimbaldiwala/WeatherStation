import serial
import time

def read_sensors(serial_port='/dev/ttyS0', baud_rate=9600, timeout=1):
    """
    Reads data from the Arduino Nano over serial communication.

    Parameters:
    serial_port (str): The serial port to use for communication.
    baud_rate (int): The baud rate for serial communication.
    timeout (int): The timeout for serial communication.

    Returns:
    dict: A dictionary containing MQ135 and rain sensor values.
    """
    ser = serial.Serial(serial_port, baud_rate, timeout=timeout)
    ser.flush()

    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            if "MQ135" in line and "Rain Sensor" in line:
                try:
                    parts = line.split(", ")
                    mq135_value = int(parts[0].split(": ")[1])
                    rain_percentage = float(parts[1].split(": ")[1].replace("%", ""))
                    return {"MQ135": mq135_value, "Rain Sensor": rain_percentage}
                except (IndexError, ValueError) as e:
                    print(f"Error parsing line: {e}")
                    continue
        time.sleep(1)

if __name__ == "__main__":
    sensor_data = read_sensors()
    print(f"MQ135 Value: {sensor_data['MQ135']}")
    print(f"Rain Sensor Percentage: {sensor_data['Rain Sensor']}%")
