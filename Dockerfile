
FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    curl \
    unzip \
    ca-certificates \
    gnupg \
    lsb-release && \
    rm -rf /var/lib/apt/lists/*

# Install AWS CLI v2
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

# Set working directory
WORKDIR /app

# Copy code
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Command to run your app
CMD ["python3", "app.py"]
