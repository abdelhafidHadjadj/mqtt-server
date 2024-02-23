FROM python:3.10

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 3000

CMD [ "python", "mqtt_pub.py", "mqtt_sub.py" ]