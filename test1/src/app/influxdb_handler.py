from influxdb import InfluxDBClient
from app.config import Config
import os

class InfluxDBHandler:
    def __init__(self):
        self.client = InfluxDBClient(
            host=Config.INFLUXDB_HOST,
            port=Config.INFLUXDB_PORT,
            username=Config.INFLUXDB_USERNAME,
            password=Config.INFLUXDB_PASSWORD,
            database=Config.INFLUXDB_DATABASE
        )
        self.inserted_files = self.load_processed_files()

    def load_processed_files(self):
        processed_files = set()
        try:
            with open(Config.PROCESSED_FILES_PATH, "r") as file:
                for line in file:
                    processed_files.add(line.strip())
        except FileNotFoundError:
            pass
        return processed_files

    def get_specific_fields(self, meas_type):
        query = f'SELECT "r_p" FROM "MME" WHERE "measType" = \'{meas_type}\''
        result = self.client.query(query)
        data_points = []
        for point in result.get_points():
            data_points.append({
                "measType": point['measType'],
                "r_p": point['r_p']
            })
        return data_points

    def insert_data(self, data_points, filename):
        try:
            
            iter(data_points)
        except TypeError:
            
            print(f"No valid data points in file '{filename}'. Skipping insertion.")
            return False
        
        try:
            if filename in self.inserted_files:
                print(f"Data from file '{filename}' already inserted. Skipping insertion.")
                return False

            json_body = [
                {
                    "measurement": "MME",
                    "tags": {
                        "measType": data_point["measType"]
                    },
                    "fields": {
                        "r_p": data_point["r_p"]
                    },
                    "time": data_point["endTime"]  # Use endTime as the timestamp
                }
                for data_point in data_points
            ]
            
            
            self.client.write_points(json_body)
            print(f"Data from file '{filename}' inserted successfully.")
            self.inserted_files.add(filename)
            self.update_processed_files(filename)  # Update processed files
            return True
        except Exception as e:
            print(f"Error inserting data from file '{filename}': {e}")
            return False

    def update_processed_files(self, filename):
        
        with open(Config.PROCESSED_FILES_PATH, "a") as file:
            file.write(filename + '\n')

