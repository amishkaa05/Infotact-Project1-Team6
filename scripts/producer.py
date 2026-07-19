#------------------------------------------
# IMPORTING LIBRARIES
#------------------------------------------

from kafka import KafkaProducer
import pandas as pd
import json
import time
from pathlib import Path


#--------------------------------------------
# CONNECT TO KAFKA
#--------------------------------------------

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)


#--------------------------------------------
# INITIALIZE VARIABLES
#--------------------------------------------

last_row = 0

csv_file = Path("data/raw/sensor_readings.csv")

#---------------------------------------------
# MONITORING SENSOR DATA
#----------------------------------------------


# The producer continuously checks for newly added sensor readings.
while True:

    # Read latest sensor data
    df = pd.read_csv(csv_file)

    # Read only newly added rows
    new_rows = df.iloc[last_row:]

    # Process one row at a time
    for index, row in new_rows.iterrows():
        # Convert one Pandas row to a Python dictionary
        sensor_data = row.to_dict()

        # Convert the dictionary to JSON
        sensor_json = json.dumps(sensor_data)

        # Send JSON data to Kafka topic
        producer.send("sensor-data",sensor_json.encode("utf-8"))

    
        print(f"Sent to kafka: {sensor_json}")
    
    # Ensure all messages are sent immediately
    producer.flush()

    # Remember the last processed row
    last_row = len(df)

    # Wait for one second before checking again
    time.sleep(1)



