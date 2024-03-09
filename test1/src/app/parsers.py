import os
import xml.etree.ElementTree as ET
from app.influxdb_handler import InfluxDBHandler

# Create a single instance of InfluxDBHandler
influxdb_handler = InfluxDBHandler()

def extract_counters(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    data_points = []

    ns = {'ns': 'http://www.3gpp.org/ftp/specs/archive/32_series/32.435#measCollec'}

    for meas_info in root.findall('.//ns:measInfo', ns):
        for meas_type in meas_info.findall('ns:measType', ns):
            meas_type_value = meas_type.text

            gran_period = meas_info.find('ns:granPeriod', ns)
            end_time = gran_period.get('endTime')

            for r in meas_info.findall('.//ns:r', ns):
                r_p = r.get('p')
                r_value = float(r.text) if r.text != 'NIL' else 0  # Handle 'NIL' value
                data_point = {
                    "measType": meas_type_value,
                    "r_p": float(r_value),  # Ensure r_value is float
                    "endTime": end_time
                }
                data_points.append(data_point)

    return data_points

def parse_and_insert_xml(file_path):
    try:
        data_points = extract_counters(file_path)
        filename = os.path.basename(file_path)
        success = influxdb_handler.insert_data(data_points, filename)
        return success  # Return success or failure directly
    except Exception as e:
        # Log any exceptions
        print(f"Error parsing and inserting data from {file_path}: {e}")
        return False  # Return False in case of any exceptions

