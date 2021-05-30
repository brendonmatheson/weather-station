#!/bin/bash

sudo docker run \
	-it --rm \
	--device /dev/i2c-1 \
	--network=weather0 \
	sensor-reader:latest

