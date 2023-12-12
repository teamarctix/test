# Use an official Ubuntu image as a parent image
FROM ubuntu:latest

# Set the working directory to /app
WORKDIR /app

# Install required packages (assuming curl, wget, and python3 are needed)
RUN apt-get update && \
    apt-get install -y curl wget python3

# Install RClone
RUN curl https://rclone.org/install.sh | bash

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get install -y python3-pip && \
    pip3 install --no-cache-dir -r requirements.txt

# Downloading config file
RUN wget -qq https://gist.githubusercontent.com/teamarctix/14298470b1a3d191624747d5f58bc84f/raw/rclone.conf -O rclone.conf

# Downloading links
RUN wget https://gist.github.com/BlackFoxy616/129bec38c78a07355588b602ca2c5152/raw/links.txt && \
    wget https://gist.github.com/BlackFoxy616/cb76be7842c810328ac99cee2f070306/raw/dled.txt

# Setup yt-dlp
RUN pip3 install yt-dlp && \
    yt-dlp --version

# Run the script when the container launches
CMD ["python3", "main.py"]
