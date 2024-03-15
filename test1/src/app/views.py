from flask import Flask, jsonify
import os
from app.parsers import parse_and_insert_xml
from app.config import Config
from app.influxdb_handler import InfluxDBHandler

app = Flask(__name__)

influxdb_handler = InfluxDBHandler()

@app.route('/test1', methods=['GET', 'POST'])
def parse_and_insert():
    """
    Parse and insert XML files into InfluxDB.
    """
    inserted_count = 0
    not_inserted_count = 0
    total_files = 0
    
    try:
        for filename in os.listdir(Config.SFTP_COLLECTION_DIRECTORY):
            if filename.endswith(".xml"):
                file_path = os.path.join(Config.SFTP_COLLECTION_DIRECTORY, filename)
                success = parse_and_insert_xml(file_path)
                if success:
                    inserted_count += 1
                else:
                    not_inserted_count += 1
                total_files += 1

    except Exception as e:
        return jsonify({"error": "An error occurred"}), 500

    return jsonify({
        "message": "Data insertion summary",
        "total_files": total_files,
        "inserted_count": inserted_count,
        "not_inserted_count": not_inserted_count
    })
