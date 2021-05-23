import bme280
import paho.mqtt.client as mqtt
import smbus2
from time import sleep

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected to MQTT broker")
	else:
		print("Failed to connect")

# Configure MQTT CLient
broker = "localhost"
port = 1883
client_id = "hea92weather01"
username = "hea92weather01"
password = "password"

client = mqtt.Client(client_id)
client.username_pw_set(username, password)
client.on_connect = on_connect
client.connect(broker, port)

port = 1
address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

base_topic = "hea92weather01"

while True:
	bme280_data = bme280.sample(bus, address)
	humidity = bme280_data.humidity
	pressure = bme280_data.pressure
	temperature = bme280_data.temperature

	print(humidity, pressure, temperature)

	client.publish(base_topic + "/humidity", humidity)
	client.publish(base_topic + "/pressure", pressure)
	client.publish(base_topic + "/temperature", temperature)

	sleep(1)

