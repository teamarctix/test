# Use the official Python image as the base image
FROM python:latest

# Install Python and pip
RUN apt-get update && apt-get install -y curl wget ffmpeg

# Install RClone
RUN curl https://rclone.org/install.sh | bash -s

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY requirements.txt .
# Install Python dependencies
RUN pip install -r requirements.
      
# Copy the entire local directory into the container
COPY . .
