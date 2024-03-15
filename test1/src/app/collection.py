import os
import pysftp
from app.config import Config

def collect_xml_files():
    """
    Collect XML files from SFTP server.
    """
    try:
        xml_files = []

        with pysftp.Connection(
            host=Config.SFTP_HOST,
            username=Config.SFTP_USERNAME,
            password=Config.SFTP_PASSWORD,
            port=Config.SFTP_PORT
        ) as sftp:
            sftp.chdir(Config.SFTP_COLLECTION_DIRECTORY)
            xml_files = sftp.listdir()

        return xml_files
    except Exception as e:
        print(f"Error collecting XML files: {e}")
        return []
