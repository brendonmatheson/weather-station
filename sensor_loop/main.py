import bme280
import paho.mqtt.client as mqtt
import smbus2
import SI1145.SI1145 as SI1145
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

#
# BME280
#

port = 1
address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

#
# GY1145 / SI1145
#

si1145 = SI1145.SI1145()

base_topic = "hea92weather01"

while True:

	# BME280
	bme280_data = bme280.sample(bus, address)
	humidity = bme280_data.humidity
	pressure = bme280_data.pressure
	temperature = bme280_data.temperature

	# SI1145
	lightVisible = si1145.readVisible()
	lightUV = si1145.readUV()
	lightIR = si1145.readIR()

	# Publish
	line = "weather,station=hea92weather01 " + \
		"humidity=" + str(humidity) + \
		",pressure=" + str(pressure) + \
		",temperature=" + str(temperature) + \
		",visible=" + str(lightVisible) + \
		",uv=" + str(lightUV) + \
		",ir=" + str(lightIR)

	print(line)

	client.publish("weather", line)

	sleep(1)

