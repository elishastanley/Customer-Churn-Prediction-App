# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary system libraries
RUN apt-get update && apt-get install -y \
    unixodbc \
    unixodbc-dev \
    g++ \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy the project files to the working directory
COPY . .

# Install the required Python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose the port your app runs on
EXPOSE 5000

# Command to run your application
CMD ["python", "home🏠.py"]
