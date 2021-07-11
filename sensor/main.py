import bme280
import os
import paho.mqtt.client as mqtt
import signal
import smbus2
import SI1145.SI1145 as SI1145
from time import sleep

default_weather_station_id = "weather01"
default_broker_client_id = "sensor"
default_broker_host_name = "broker_mosquitto_1"
default_broker_port = 1883
default_broker_username = "username"
default_broker_password = "password"
default_sample_interval = 15

class SensorReader:

	def __init__(self):
		self.stopped = False

	def run( \
		self, \
		weather_station_id, \
		broker_client_id, \
		broker_host_name, \
		broker_port, \
		broker_username, \
		broker_password, \
		sample_interval):

		#
		# Configure MQTT Client
		#

		def mqtt_on_connect(client, userdata, flags, rc):
			if rc == 0:
				print("Connected to MQTT broker")
				client.connected_flag = True
			else:
				print("Failed to connect")

		def mqtt_on_disconnect(client, userdata, rc):
			print("Disconnecting reason " + str(rc))
			client.connected_flag = False
			client.disconnect_flag = True

		client = mqtt.Client(broker_client_id)
		client.on_connect = mqtt_on_connect
		client.on_disconnect = mqtt_on_disconnect
		client.connected_flag = False
		client.username_pw_set(broker_username, broker_password)
		client.connect(broker_host_name, broker_port)
		client.loop_start()

		while not self.stopped and not client.connected_flag:
			print("Waiting for connection")
			sleep(1)

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

		while not self.stopped:

			if (client.connected_flag):

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
				influx = "weather,station=" + weather_station_id + " " + \
					"humidity=" + str(humidity) + \
					",pressure=" + str(pressure) + \
					",temperature=" + str(temperature) + \
					",visible=" + str(lightVisible) + \
					",uv=" + str(lightUV) + \
					",ir=" + str(lightIR)

				print(influx)

				client.publish("weather/" + weather_station_id + "/influx", influx)
				client.publish("weather/" + weather_station_id + "/humidity", humidity)
				client.publish("weather/" + weather_station_id + "/pressure", pressure)
				client.publish("weather/" + weather_station_id + "/temperature", temperature)
				client.publish("weather/" + weather_station_id + "/visible", lightVisible)
				client.publish("weather/" + weather_station_id + "/uv", lightUV)
				client.publish("weather/" + weather_station_id + "/ir", lightIR)

				sleep(sample_interval)

			else:
				print("Connection lost.  Waiting for reconnection")
				sleep(5)

		client.loop_stop()
		client.disconnect()

	def stop(self, signal, frame):
		print("Stopping SensorReader")
		self.stopped = True

def main():

	weather_station_id = os.getenv("WEATHER_STATION_ID")
	if (weather_station_id == None):
		weather_station_id = default_weather_station_id

	broker_client_id = os.getenv("BROKER_CLIENT_ID")
	if (broker_client_id == None):
		broker_client_id = default_broker_client_id

	broker_host_name = os.getenv("BROKER_HOST_NAME")
	if (broker_host_name == None):
		broker_host_name = default_broker_host_name

	broker_port = os.getenv("BROKER_PORT")
	if (broker_port == None):
		broker_port = default_broker_port

	broker_username = os.getenv("BROKER_USERNAME")
	if (broker_username == None):
		broker_username = default_broker_username

	broker_password = os.getenv("BROKER_PASSWORD")
	if (broker_password == None):
		broker_password = default_broker_password

	sample_interval = os.getenv("SAMPLE_INTERVAL")
	if (sample_interval == None):
		sample_interval = default_sample_interval

	sample_interval = int(sample_interval)

	print("Configuration:")
	print("+ weather_station_id: " + str(weather_station_id))
	print("+ broker_client_id: " + str(broker_client_id))
	print("+ broker_host_name: " + str(broker_host_name))
	print("+ broker_port: " + str(broker_port))
	print("+ broker_username: " + str(broker_username))
	print("+ broker_password: " + str(broker_password))
	print("+ sample_interval: " + str(sample_interval))

	sensorReader = SensorReader()
	signal.signal(signal.SIGINT, sensorReader.stop)
	signal.signal(signal.SIGTERM, sensorReader.stop)

	sensorReader.run( \
		weather_station_id, \
		broker_client_id, \
		broker_host_name, \
		broker_port, \
		broker_username, \
		broker_password, \
		sample_interval)

if __name__ == "__main__":
	main()

