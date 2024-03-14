FROM python:3.10

# Set the working directory
WORKDIR /src

# Copy requirements.txt and install dependencies
COPY requirements.txt /src
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /src

# Expose any ports your app needs
 EXPOSE 8089

# Command to run the application
CMD ["python", "run1.py"]
