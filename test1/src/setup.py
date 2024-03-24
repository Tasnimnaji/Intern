import os
import subprocess
import datetime
from setuptools import setup, find_packages

def generate_snapshot_version():
    """
    Generate a snapshot version based on the current date and time.
    Returns:
        str: Snapshot version string.
    """
    now = datetime.datetime.now()
    version = now.strftime("%Y%m%d%H%M%S")
    return version + "-SNAPSHOT"

def upload_to_nexus():
    """
    Upload the package to Nexus repository.
    """
    nexus_url = 'http://192.168.33.10:8081/repository/app/'
    username = 'admin'
    password = 'nexus'

    snapshot_version = generate_snapshot_version()

    with open('setup.py', 'r', encoding='utf-8') as file:
        setup_content = file.read()
    setup_content = setup_content.replace("version='1.0.0.dev0'", f"version='{snapshot_version}'")
    with open('setup.py', 'w', encoding='utf-8') as file:
        file.write(setup_content)

    publish_command = ['python3', 'setup.py', 'sdist']
    subprocess.run(publish_command, check=True)

    upload_command = ['twine', 'upload', '--repository-url', nexus_url, '-u', username, '-p', password, '--skip-existing', 'dist/*']
    subprocess.run(upload_command, check=True)

# Read the requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

if os.getenv('UPLOAD_PACKAGE') == '1':
    upload_to_nexus()

setup(
    name='test1',
    version='1.0.0.dev0',
    author='Tasnim NAJI',
    author_email='tasnim.naji@esprit.tn',
    description='End of Year project',
    packages=find_packages(),
    install_requires=requirements,
    data_files=[('', ['requirements.txt'])],
)
