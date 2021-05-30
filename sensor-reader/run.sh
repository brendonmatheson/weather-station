#!/bin/bash

sudo docker run \
	-it --rm \
	--device /dev/i2c-1 \
	sensor-reader:latest

