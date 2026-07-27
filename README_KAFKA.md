Kafka Streaming Module





\## Overview



This module implements the Kafka streaming layer for the AtmoSync project.



The IoT simulator developed by Amishka generates sensor data and stores it in sensor\_readings.csv. After pulling the latest project from GitHub, the generated sensor data was used as the input for developing and testing the Kafka Producer and Kafka Consumer.



\------------------------------------------------------------------------------------------------------------



\## Module Responsibilities



\- Implement Kafka Producer

\- Implement Kafka Consumer

\- Stream real-time sensor data

\- Verify end-to-end Kafka pipeline

\- Prepare data for Snowflake integration



\------------------------------------------------------------------------------------------------------------



\## Project Workflow





IoT Simulator (Amishka)

&#x20;       │

&#x20;       ▼

sensor\_readings.csv

&#x20;       │

&#x20;       ▼

Kafka Producer

&#x20;       │

&#x20;       ▼

Kafka Topic (sensor-data)

&#x20;       │

&#x20;       ▼

Kafka Consumer

&#x20;       │

&#x20;       ▼

Ready for Snowflake Integration





\--------------------------------------------------------------------------------------------------------------



\## Files



scripts/

|---producer.py

|---consumer.py





\--------------------------------------------------------------------------------------------------------------



\## Technologies Used



\- Python

\- Apache Kafka

\- Pandas

\- JSON



\--------------------------------------------------------------------------------------------------------------



\## How to Run



\### 1. Start Kafka



```bash

bin\\windows\\kafka-server-start.bat config\\server.properties

```



\### 2. Run Simulator



```bash

python scripts\\simulator.py

```



\### 3. Run Producer



```bash

python scripts\\producer.py

```



\### 4. Run Consumer



```bash

python scripts\\consumer.py

```



\--------------------------------------------------------------------------------------------------------------



\## Current Status



\- Kafka Producer Completed

\- Kafka Consumer Completed

\- End-to-End Pipeline Verified

\- Ready for Snowflake Integration

