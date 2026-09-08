CREATE DATABASE atmosync_db;
USE atmosync_db;
SHOW DATABASES;
USE atmosync_db;

CREATE TABLE sensor_data (
    Container_ID VARCHAR(20),
    Commodity VARCHAR(50),
    Origin VARCHAR(50),
    Destination VARCHAR(50),
    Temperature_C DECIMAL(5,2),
    Humidity_Percent DECIMAL(5,2),
    Vibration_g DECIMAL(5,2),
    Latitude DECIMAL(10,6),
    Longitude DECIMAL(10,6),
    Timestamp DATETIME,
    Sensor_Status VARCHAR(20),
    Battery_Level INT,
    Transport_Mode VARCHAR(30)
);

SHOW TABLES;
DESCRIBE sensor_data;

SELECT COUNT(*) AS total_records
FROM iot_sensor_dataset_1000_rows;

SELECT *
FROM iot_sensor_dataset_1000_rows
LIMIT 10;

SELECT
    SUM(Container_ID IS NULL) AS Missing_Container_ID,
    SUM(Commodity IS NULL) AS Missing_Commodity,
    SUM(Temperature_C IS NULL) AS Missing_Temperature,
    SUM(Humidity_Percent IS NULL) AS Missing_Humidity,
    SUM(Battery_Level IS NULL) AS Missing_Battery
FROM iot_sensor_dataset_1000_rows;

SELECT
    Container_ID,
    COUNT(*) AS record_count
FROM iot_sensor_dataset_1000_rows
GROUP BY Container_ID
HAVING COUNT(*) > 1;

SELECT
    AVG(Temperature_C) AS Average_Temperature
FROM iot_sensor_dataset_1000_rows;

SELECT
    MIN(Temperature_C) AS Minimum_Temperature,
    MAX(Temperature_C) AS Maximum_Temperature
FROM iot_sensor_dataset_1000_rows;

SELECT
    Commodity,
    COUNT(*) AS Total_Readings,
    ROUND(AVG(Temperature_C), 2) AS Avg_Temperature,
    ROUND(AVG(Humidity_Percent), 2) AS Avg_Humidity
FROM iot_sensor_dataset_1000_rows
GROUP BY Commodity
ORDER BY Total_Readings DESC;

SELECT
    Transport_Mode,
    COUNT(*) AS Total_Readings,
    ROUND(AVG(Vibration_g), 2) AS Avg_Vibration
FROM iot_sensor_dataset_1000_rows
GROUP BY Transport_Mode
ORDER BY Avg_Vibration DESC;

SELECT *
FROM iot_sensor_dataset_1000_rows
WHERE Temperature_C > 10;

SELECT
    Container_ID,
    Battery_Level,
    Sensor_Status
FROM iot_sensor_dataset_1000_rows
WHERE Battery_Level < 30
ORDER BY Battery_Level ASC;

SELECT
    Sensor_Status,
    COUNT(*) AS Total_Sensors
FROM iot_sensor_dataset_1000_rows
GROUP BY Sensor_Status;

SELECT
    Origin,
    Destination,
    COUNT(*) AS Total_Shipments
FROM iot_sensor_dataset_1000_rows
GROUP BY Origin, Destination
ORDER BY Total_Shipments DESC;

SELECT
    DATE(Timestamp) AS Reading_Date,
    COUNT(*) AS Total_Readings
FROM iot_sensor_dataset_1000_rows
GROUP BY DATE(Timestamp)
ORDER BY Reading_Date;

SELECT COUNT(*) FROM iot_sensor_dataset_1000_rows;

SELECT MIN(Timestamp), MAX(Timestamp)
FROM iot_sensor_dataset_1000_rows;

SELECT COUNT(DISTINCT Container_ID)
FROM iot_sensor_dataset_1000_rows;

SELECT COUNT(DISTINCT Commodity)
FROM iot_sensor_dataset_1000_rows;

SELECT COUNT(DISTINCT Transport_Mode)
FROM iot_sensor_dataset_1000_rows;