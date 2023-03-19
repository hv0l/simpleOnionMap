# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the script into the container
COPY onion_scan.py .

# Install additional dependencies (Tor, Nmap, Proxychains)
RUN apt-get update && \
    apt-get install -y tor nmap proxychains && \
    rm -rf /var/lib/apt/lists/*

# Run the script when the container is started
ENTRYPOINT ["python3", "onion_scan.py"]
