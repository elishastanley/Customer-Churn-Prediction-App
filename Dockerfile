# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install necessary system libraries
RUN apt-get update && apt-get install -y \
    curl \
    unixodbc \
    unixodbc-dev \
    g++ \
    gcc \
    gnupg \
    apt-transport-https \
    && rm -rf /var/lib/apt/lists/*

# Add Microsoft repository for the ODBC driver
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list

# Install Microsoft ODBC Driver for SQL Server
RUN apt-get update && ACCEPT_EULA=Y DEBIAN_FRONTEND=noninteractive apt-get install -y msodbcsql17 \
    -o Dpkg::Options::="--force-overwrite"

# Clean up the apt cache to reduce image size
RUN apt-get clean && rm -rf /var/lib/apt/lists/*


# Copy the project files to the working directory
COPY . .

# Install the required Python packages
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Expose the port your app runs on
EXPOSE 5000

# Command to run your application
CMD ["streamlit", "run", "app.py", "--server.port=5000", "--server.address=0.0.0.0"]

