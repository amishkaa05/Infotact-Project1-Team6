import pandas as pd
import random
import time
from datetime import datetime
import csv
import os

# ==========================
# LOAD CSV FILES
# ==========================

commodities = pd.read_csv("data/sample/commodities.csv")
containers = pd.read_csv("data/sample/containers.csv")

# ==========================
# MERGE DATA
# ==========================

container_data = pd.merge(
    containers,
    commodities,
    on="commodity"
)

print("\n=== MERGED DATA ===")
print(container_data)

# ==========================
# CREATE OUTPUT CSV
# ==========================

output_file = "data/raw/sensor_readings.csv"

if not os.path.exists(output_file):

    with open(output_file, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "timestamp",
            "container_id",
            "commodity",
            "temperature",
            "humidity",
            "vibration",
            "status",
            "origin",
            "destination"
        ])

# ==========================
# GENERATE SENSOR DATA
# ==========================

def generate_sensor_data():

    print("\nGenerating Sensor Data...\n")

    for _, row in container_data.iterrows():

        # --------------------------
        # Generate Normal Sensor Values
        # --------------------------

        temperature = round(
            random.uniform(row["min_temp"], row["max_temp"]),
            1
        )

        humidity = round(
            random.uniform(row["min_humidity"], row["max_humidity"]),
            1
        )

        vibration = round(
            random.uniform(0.2, 2.5),
            2
        )

        # --------------------------
        # 5% Chance of Anomaly
        # --------------------------

        if random.random() < 0.05:

            temperature = round(
                random.uniform(
                    row["max_temp"] + 5,
                    row["max_temp"] + 15
                ),
                1
            )

            humidity = round(
                random.uniform(
                    row["max_humidity"] + 5,
                    100
                ),
                1
            )

            vibration = round(
                random.uniform(3.5, 6.0),
                2
            )

        # --------------------------
        # Generate Timestamp
        # --------------------------

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # --------------------------
        # Calculate Status
        # --------------------------

        if (
            temperature > row["max_temp"]
            or humidity > row["max_humidity"]
            or vibration > 3
        ):
            status = "CRITICAL"
        else:
            status = "NORMAL"

        # --------------------------
        # Print Sensor Data
        # --------------------------

        print(f"Timestamp   : {timestamp}")
        print(f"Container   : {row['container_id']}")
        print(f"Commodity   : {row['commodity']}")
        print(f"Temperature : {temperature} °C")
        print(f"Humidity    : {humidity} %")
        print(f"Vibration   : {vibration}")
        print(f"Status      : {status}")
        print("----------------------------------------")

        # --------------------------
        # Save Reading to CSV
        # --------------------------

        with open(output_file, "a", newline="") as file:

            writer = csv.writer(file)

            writer.writerow([
                timestamp,
                row["container_id"],
                row["commodity"],
                temperature,
                humidity,
                vibration,
                status,
                row["origin"],
                row["destination"]
            ])

# ==========================
# RUN SIMULATOR CONTINUOUSLY
# ==========================

while True:

    generate_sensor_data()

    # Wait 1 second before generating the next batch
    time.sleep(1)