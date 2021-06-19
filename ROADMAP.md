# Roadmap

## Backlog

| ID              | Summary                                                      | Notes                                                        | Status      | LU         |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------- | ---------- |
|                 |                                                              |                                                              |             |            |
| **Prioritized** |                                                              |                                                              |             |            |
|                 |                                                              |                                                              |             |            |
| WST-33          | Home Assistant Integration                                   |                                                              | In Progress | 2021-06-02 |
| WST-7           | Check and set the QoS params for MQTT messages to ensure best delivery rate |                                                              |             |            |
| WST-6           | Tune retention settings for on-station InfluxDB              |                                                              |             |            |
| WST-8           | Setup on-prem InfluxDB using v2.x                            |                                                              | In Progress | 2021-06-01 |
| WST-9           | Update Grafana config to use on-prem InfluxDB                |                                                              | In Progress | 2021-06-02 |
|                 |                                                              |                                                              |             |            |
| **Backlog**     |                                                              |                                                              |             |            |
|                 |                                                              |                                                              |             |            |
| WST-1           | Endurance test of the 18650 UPS board                        | First endurance test ran for almost 16 hours - this was while SSD was out of action so was using SD card.  Will re-test on 52pi board when it arrives. | In Progress | 2021-05-30 |
| WST-2           | Measure power consumption of the 18650 UPS board when charging from empty on mains | Tested on current board.  Will re-test on 52pi board when it arrives. | In Progress | 2021-06-02 |
| WST-3           | Measure power consumption of the 18650 UPS board when charging from empty on PoE+ | Tested on current board.  Will re-test on 52pi board when it arrives. | In Progress | 2021-06-02 |
| WST-10          | Create insta-launchable Grafana config for users of this project. | Not needed for my own requirements as I already have a full Prometheus / Grafana stack. |             |            |
| WST-11          | RJ-11 connectors for all sensors.                            | To be done after all or most sensors have been prototyped.  Also need to consider the physical enclosure design to choose the right length for RJ-11 cables. |             |            |
| WST-12          | IP67 enclosure.                                              | Preferrably with a clear window.  Possibly with a 3D printed add-on shroud underneath to mount sensors. |             |            |
| WST-13          | Sensor / Lightning / AS3935                                  |                                                              |             |            |
| WST-15          | Sensor / Ground Temperature / DS18B20                        |                                                              |             |            |
| WST-17          | Sensor / Ground Moisture / TBD                               |                                                              |             |            |
| WST-18          | Sensor / Gas / MQ-2                                          | LPG, Propane, Hydrogen, Methane, Smoke.  [How it works](https://lastminuteengineers.com/mq2-gas-senser-arduino-tutorial/) |             |            |
| WST-19          | Sensor / Gas / MQ-4                                          | LPG, Methane                                                 |             |            |
| WST-20          | Sensor / Gas / MQ-5                                          | LPG, Methane                                                 |             |            |
| WST-21          | Sensor / Gas / MQ-7                                          | Carbon Monoxide                                              |             |            |
| WST-22          | Sensor / Gas / MQ-135                                        | Ammonia, Sulfide, Benzene                                    |             |            |
| WST-23          | Sensor / Wind Speed / Misol Anemomoeter                      |                                                              |             |            |
| WST-24          | Sensor / Wind Direction / Misol Wind Vane                    |                                                              |             |            |
| WST-25          | Sensor / Rain Fall / Misol Rain Gauge                        |                                                              |             |            |
| WST-26          | Sensor / PM 2.5 / PMS5003                                    |                                                              |             |            |
| WST-28          | Stevenson screened enclosure                                 |                                                              |             |            |
| WST-31          | Weather simulator                                            | To make it easy to get up and running for new users of this stack - a containerized script that simulates real weather station harware by publishing generated values to the MQTT topics.  Enables you to run the data plane with no hardware to see it working before you start adding sensors. |             |            |
| WST-34          | Replace UPS board                                            | 52pi's board seems to be the best available: https://wiki.52pi.com/index.php/UPS_(With_RTC_%26_Coulometer)_For_Raspberry_Pi_SKU:_EP-0118 |             |            |
|                 |                                                              |                                                              |             |            |
| **New**         | 35                                                           |                                                              |             |            |
|                 |                                                              |                                                              |             |            |
| WST-35          | US Power Outages                                             | Integrate data from https://poweroutage.us/ possibly using https://grafana.com/grafana/plugins/grafana-worldmap-panel/ |             |            |
|                 |                                                              |                                                              |             |            |
| **Complete**    |                                                              |                                                              |             |            |
|                 |                                                              |                                                              |             |            |
| WST-16          | Sensor / Atmosphere / BME280                                 |                                                              | Complete    | 2021-05-23 |
| WST-27          | Make local-storage automatically start on boot               |                                                              | Complete    | 2021-05-26 |
| WST-14          | Sensor / Sunlight / GY1145                                   | Visible / UV-A / UV-B.  Also test to see how much, if any, of the UV-C spectrum it can see. | Complete    | 2021-05-26 |
| WST-30          | Wrap sensor_loop in a Docker image                           |                                                              | Complete    | 2021-05-30 |
| WST-29          | Reconnect MQTT when dropped                                  |                                                              | Complete    | 2021-06-01 |
| WST-32          | Parameterize                                                 | Currently many values are hardcoded for my environment.  Need to parameterize so that others could use it. | Complete    | 2021-06-01 |
| WST-4           | External activity LED                                        |                                                              | Complete    | 2021-05-29 |
| WST-5           | 3D printed mount for PoE+ adapter                            | This is assuming the PoE+ adapter passes the power consumption tests | Complete    | 2021-05-28 |
|                 |                                                              |                                                              |             |            |

