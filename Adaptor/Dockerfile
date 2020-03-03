FROM python

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install paho-mqtt influxdb

ADD ./adaptor.py /app/adaptor.py

WORKDIR /app

CMD ["python", "adaptor.py"]