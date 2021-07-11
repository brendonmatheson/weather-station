import I2C_LCD_driver
import os
import paho.mqtt.client as mqtt
import signal
import time

default_client_id = "hea92weather01-lcd"
default_broker_host_name = "broker_mosquitto_1"
default_broker_port = 1883
default_broker_username = "username"
default_broker_password = "password"

LCD = I2C_LCD_driver.lcd()

class Subscriber:

	def __init__(self):
		self.stopped = False
		self.temperature = None
		self.humidity = None
		self.pressure = None
		self.light_visible = None
		self.light_ir = None
		self.light_uv = None

	def run( \
		self, \
		client_id, \
		broker_host_name, \
		broker_port, \
		broker_username, \
		broker_password):

		LCD.lcd_clear()
		self.show_page("", self.center("Initializing"), "", "")
		time.sleep(2)

		#
		# Configure MQTT Client
		#

		def mqtt_on_connect(client, userdata, flags, rc):
			if rc == 0:
				print("MQTT connected")
				client.connected_flag = True
				client.subscribe("weather/hea92weather01/#", qos=0)
			else:
				print("Connection Failed")

		def mqtt_on_disconnect(client, userdata, rc):
			print("Disconnected with reason: " + str(rc))
			client.connected_flag = False

		def mqtt_on_subscribe(client, userdata, mid, granted_qos):
			print("Subscribed")

		def mqtt_on_unsubscribe(client, userdata, mid):
			print("Unsubscribed")

		def mqtt_on_message(client, userdata, message):
			payload = str(message.payload.decode("utf-8"))
			#print("message received", str(message.topic), payload)

			if message.topic == "weather/hea92weather01/temperature":
				self.temperature = float(payload)
			if message.topic == "weather/hea92weather01/humidity":
				self.humidity = float(payload)
			if message.topic == "weather/hea92weather01/pressure":
				self.pressure = float(payload)
			if message.topic == "weather/hea92weather01/visible":
				self.light_visible = int(payload)
			if message.topic == "weather/hea92weather01/ir":
				self.light_ir = int(payload)
			if message.topic == "weather/hea92weather01/uv":
				self.light_uv = int(payload)


		client = mqtt.Client(client_id)
		client.on_connect = mqtt_on_connect
		client.on_disconnect = mqtt_on_disconnect
		client.on_subscribe = mqtt_on_subscribe
		client.on_unsubscribe = mqtt_on_unsubscribe
		client.on_message = mqtt_on_message
		client.connected_flag = False
		client.username_pw_set(broker_username, broker_password)
		client.connect(broker_host_name, broker_port)

		client.loop_start()

		while not self.stopped and not client.connected_flag:
			self.show_page("", self.center("Connecting MQTT"), "", "")
			time.sleep(1)

		# page is 1-baesd
		pages = 2
		page = 1

		while not self.stopped:

			if client.connected_flag:

				for x in range(5):
					if self.stopped:
						break
					if (page == 1):
						self.show_page_1()
					elif (page == 2):
						self.show_page_2()

					time.sleep(1)

				page += 1
				if (page > pages):
					print("Advancing page")
					page = 1

			else:
				print("MQTT connection lost")
				self.show_page( \
					"", \
					"MQTT connection lost", \
					"Trying to reconnect", \
					"")
				time.sleep(5)

		client.loop_stop()
		client.disconnect()

	def show_page(self, line1, line2, line3, line4):
		# If line is less than 20 chars pad, if more truncate.  We want the line to be
		# exactly 20 chars so it overwrites whatever was there before, but not more
		# because overflowing causes the LCD display to show junk characters and get
		# into a bad state
		line1 = "{:<20}".format(line1)[:20]
		line2 = "{:<20}".format(line2)[:20]
		line3 = "{:<20}".format(line3)[:20]
		line4 = "{:<20}".format(line4)[:20]

		LCD.lcd_display_string("{:<20}".format(line1)[:20], 1)
		LCD.lcd_display_string("{:<20}".format(line2)[:20], 2)
		LCD.lcd_display_string("{:<20}".format(line3)[:20], 3)
		LCD.lcd_display_string("{:<20}".format(line4)[:20], 4)

	def show_page_1(self):
		self.show_page(
			self.line_element_float("Tmp", self.temperature, "C"), \
			self.line_element_float("Hum", self.humidity, "%"), \
			self.line_element_int("Prs", self.pressure, "mb"), \
			"")

	def show_page_2(self):
		self.show_page( \
			self.line_element_int("Vis", self.light_visible, "L"), \
			self.line_element_int("IR", self.light_ir, "L"), \
			self.line_element_int("UV", self.light_uv, "L"), \
			"")

	def line_element_int(self, label, value, unit):
		label_length = len(label) + 1
		unit_length = len(unit)

		element = ""
		if value == None:
			value_length = 10 - label_length
			format_string = "{0}:{1:^" + str(value_length) + "}"
			element = format_string.format(label, "--")

		else:
			value_length = 10 - label_length - unit_length
			format_string = "{0}:{1:>" + str(value_length) + "d}{2}"
			element = format_string.format(label, int(value), unit)

		return element

	def line_element_float(self, label, value, unit):
		label_length = len(label) + 1
		unit_length = len(unit)

		element = ""
		if value == None:
			value_length = 10 - label_length
			format_string = "{0}:{1:^" + str(value_length) + "}"
			element = format_string.format(label, "--")

		else:
			value_length = 10 - label_length - unit_length
			format_string = "{0}:{1:>" + str(value_length) + ".1f}{2}"
			element = format_string.format(label, value, unit)

		return element

	def center(self, message):
		return "{:^20}".format(message)[:20]

	def stop(self, signal, frame):
		self.show_page("", self.center("Stopping"), "", "")
		self.stopped = True

def main():


	client_id = os.getenv("CLIENT_ID")
	if (client_id == None):
		client_id = default_client_id

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

	print("Configuration:")
	print("+ client_id: " + str(client_id))
	print("+ broker_host_name: " + str(broker_host_name))
	print("+ broker_port: " + str(broker_port))
	print("+ broker_username: " + str(broker_username))
	print("+ broker_password: " + str(broker_password))

	subscriber = Subscriber()
	signal.signal(signal.SIGINT, subscriber.stop)
	signal.signal(signal.SIGTERM, subscriber.stop)

	subscriber.run( \
		client_id, \
		broker_host_name, \
		broker_port, \
		broker_username, \
		broker_password)

if __name__ == "__main__":
	main()

