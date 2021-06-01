import bme280
import paho.mqtt.client as mqtt
import signal
import smbus2
import SI1145.SI1145 as SI1145
from time import sleep

class SensorReader:

	def __init__(self):
		self.stopped = False

	def run(self):

		#
		# Configure MQTT CLient
		#

		broker = "broker_mosquitto_1"
		port = 1883
		client_id = "hea92weather01"
		username = "hea92weather01"
		password = "password"

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

		client = mqtt.Client(client_id)
		client.on_connect = mqtt_on_connect
		client.on_disconnect = mqtt_on_disconnect
		client.connected_flag = False
		client.username_pw_set(username, password)
		client.connect(broker, port)
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

		weather_station_id = "hea92weather01"

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
				influx = "weather,station=hea92weather01 " + \
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

				sleep(1)

			else:
				print("Connection lost.  Waiting for reconnection")
				sleep(5)

		client.loop_stop()
		client.disconnect()

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

