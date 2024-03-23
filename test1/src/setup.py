import os
from setuptools import setup, find_packages

# Get the absolute path to the directory containing setup.py
base_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the full path to requirements.txt
requirements_file = os.path.join(base_dir, 'requirements.txt')

# Read the contents of requirements.txt for dependencies
with open(requirements_file) as f:
    requirements = f.read().splitlines()
import os
from setuptools import setup, find_packages
import subprocess

# Get the absolute path to the directory containing setup.py
base_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the full path to requirements.txt
requirements_file = os.path.join(base_dir, 'requirements.txt')

# Read the contents of requirements.txt for dependencies
with open(requirements_file) as f:
    requirements = f.read().splitlines()

# Define the upload_to_nexus function
def upload_to_nexus():
    # Nexus repository URL, username, and password
    nexus_url = 'http://192.168.33.10:8081/repository/app/'
    username = 'admin'
    password = 'nexus'

    # Command to create the source distribution package
    publish_command = ['python3', 'setup.py', 'sdist']

    # Execute the publish command
    subprocess.run(publish_command, check=True)

    # Command to publish the package to Nexus using twine
    upload_command = ['twine', 'upload', '--repository-url', nexus_url, '-u', username, '-p', password, '--skip-existing', 'dist/*']

    # Execute the upload command
    subprocess.run(upload_command, check=True)

# Call the upload_to_nexus function if UPLOAD_PACKAGE environment variable is set to 1
if os.getenv('UPLOAD_PACKAGE') == '1':
    upload_to_nexus()

# Setup function to define the package metadata
setup(
    name='test1',
    version='1.0.0.dev0',
    author='Tasnim NAJI',
    author_email='tasnim.naji@esprit.tn',
    description='End of Year project',
    packages=find_packages(),
    install_requires=requirements,
    data_files=[('', ['requirements.txt'])],  # Include requirements.txt in the package
)


setup(
    name='test1',
    version='1.0.0.dev0',
    author='Tasnim NAJI',
    author_email='tasnim.naji@esprit.tn',
    description='End of Year project',
    packages=find_packages(),
    install_requires=requirements,
    data_files=[('', ['requirements.txt'])]  # Include requirements.txt in the package
)

