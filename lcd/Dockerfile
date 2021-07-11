FROM python:3.9.5-buster

RUN mkdir /app
WORKDIR /app

copy I2C_LCD_driver.py ./
COPY main.py ./

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "./main.py" ]

