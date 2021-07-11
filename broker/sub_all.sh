#!/bin/bash

# Copyright (c) 2021, Aleisium
#
# http://aleisium.com/
#
# This document is copyright.  You may not reproduce or transmit it any any
# form or by any means without permission in writing from the owner of this
# work, Aleisium.  If you infringe our copyright, you render yourself liable
# for prosecution.

sudo docker exec -it broker_mosquitto_1 mosquitto_sub -t "#" -u "hea92weather01" -P "password" -v

