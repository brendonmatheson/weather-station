import bme280
import smbus2
from time import sleep

port = 1
address = 0x76
bus = smbus2.SMBus(port)

bme280.load_calibration_params(bus,address)

while True:
	bme280_data = bme280.sample(bus, address)
	humidity = bme280_data.humidity
	pressure = bme280_data.pressure
	temperature = bme280_data.temperature

	print(humidity, pressure, temperature)

	sleep(1)

print("hi bren")

