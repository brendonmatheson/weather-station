# Roadmap

## Backlog

| ID              | Summary                                                      | Notes                                                        | Status      | LU         |
| --------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------- | ---------- |
|                 |                                                              |                                                              |             |            |
| **Prioritized** |                                                              |                                                              |             |            |
|                 |                                                              |                                                              |             |            |
| WST-1           | Endurance test of the 18650 UPS board                        |                                                              |             |            |
| WST-2           | Measure power consumption of the 18650 UPS board when charging from empty on mains |                                                              |             |            |
| WST-3           | Measure power consumption of the 18650 UPS board when charging from empty on PoE+ |                                                              |             |            |
| WST-29          | Reconnect MQTT when dropped                                  |                                                              | In Progress | 2021-05-26 |
| WST-7           | Check and set the QoS params for MQTT messages to ensure best delivery rate |                                                              |             |            |
| WST-6           | Tune retention settings for on-station InfluxDB              |                                                              |             |            |
| WST-8           | Setup on-prem InfluxDB using v2.x                            |                                                              |             |            |
| WST-9           | Update Grafana config to use on-prem InfluxDB                |                                                              |             |            |
|                 |                                                              |                                                              |             |            |
| **Backlog**     |                                                              |                                                              |             |            |
|                 |                                                              |                                                              |             |            |
| WST-4           | External activity LED                                        |                                                              |             |            |
| WST-5           | 3D printed mount for PoE+ adapter                            | This is assuming the PoE+ adapter passes the power consumption tests |             |            |
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
|                 |                                                              |                                                              |             |            |
| **Complete**    |                                                              |                                                              |             |            |
|                 |                                                              |                                                              |             |            |
| WST-16          | Sensor / Atmosphere / BME280                                 |                                                              | Complete    | 2021-05-23 |
| WST-27          | Make local-storage automatically start on boot               |                                                              | Complete    | 2021-05-26 |
| WST-14          | Sensor / Sunlight / GY1145                                   | Visible / UV-A / UV-B.  Also test to see how much, if any, of the UV-C spectrum it can see. | Complete    | 2021-05-26 |
| WST-30          | Wrap sensor_loop in a Docker image                           |                                                              | Complete    | 2021-05-30 |
|                 |                                                              |                                                              |             |            |

