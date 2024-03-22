import os
from setuptools import setup, find_packages

# Get the absolute path to the directory containing setup.py
base_dir = os.path.dirname(os.path.abspath(__file__))

# Specify the full path to requirements.txt
requirements_file = os.path.join(base_dir, 'requirements.txt')

# Read the contents of requirements.txt for dependencies
with open(requirements_file) as f:
    requirements = f.read().splitlines()

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

