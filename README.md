# Heathcote Weather Station 1

## Hardware Platform

- Raspberry Pi 3B
- X702 UPS Board with two 18650 cells (TODO which brand)
- Transcend 128GB SSD

## Operating System Configuration

### Enable SSD Boot

This is a one-off change - now that it has been done, this Raspberry Pi is permanently configured to allow SSD boot.

### Docker

Install Docker using the [convenience script](https://docs.docker.com/engine/install/debian/#install-using-the-convenience-script) from the Docker site.

Install docker-compose:

```bash
# Dependencies
sudo apt-get install -y libffi-dev libssl-dev
sudo apt install -y python3-dev
sudo apt-get install -y python3 python3-pip

# docker-compose
sudo pip3 install docker-compose
```

References:

- https://devdojo.com/bobbyiliev/how-to-install-docker-and-docker-compose-on-raspberry-pi

### Prometheus Exporters

See `als_sys_container_telemetry` for full details.

Exporters installed:

- rpi_exporter
- node_exporter
- Docker Engine
- cAdvisor

