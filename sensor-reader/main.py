import bme280
import paho.mqtt.client as mqtt
import signal
import smbus2
import SI1145.SI1145 as SI1145
from time import sleep

def mqtt_on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("Connected to MQTT broker")
	else:
		print("Failed to connect")

class SensorReader:

	def __init__(self):
		self.stopped = False

	def run(self):

		#
		# Configure MQTT CLient
		#

		broker = "10.80.2.31"
		port = 1883
		client_id = "hea92weather01"
		username = "hea92weather01"
		password = "password"

		client = mqtt.Client(client_id)
		client.username_pw_set(username, password)
		client.on_connect = mqtt_on_connect
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

		while not self.stopped:
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

	def stop(self, signal, frame):
		print("Stopping SensorReader")
		self.stopped = True

def main():
	sensorReader = SensorReader()
	signal.signal(signal.SIGINT, sensorReader.stop)
	signal.signal(signal.SIGTERM, sensorReader.stop)
	sensorReader.run()

if __name__ == "__main__":
	main()

