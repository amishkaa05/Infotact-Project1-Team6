#------------------------------------------
# IMPORTING LIBRARIES
#------------------------------------------

from kafka import KafkaConsumer
import json


#------------------------------------------
# CONNECT TO KAFKA
#------------------------------------------

consumer = KafkaConsumer("sensor-data",bootstrap_servers="localhost:9092"
)


#------------------------------------------
# READ MESSAGES FROM KAFKA
#------------------------------------------

print("Waiting for sensor data...\n")

# Continuously listen for new messages
for message in consumer:

    # Convert bytes to string
    sensor_json = message.value.decode("utf-8")

    # Convert JSON string to Python dictionary
    sensor_data = json.loads(sensor_json)

    # Display received data
    print(sensor_data)







