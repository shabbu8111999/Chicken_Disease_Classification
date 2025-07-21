FROM python:3.10-slim-buster

# Install required system packages for awscli and unzip
RUN apt-get update && \
    apt-get install -y curl unzip && \
    curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
    unzip awscliv2.zip && \
    ./aws/install && \
    rm -rf awscliv2.zip aws

# Set the working directory
WORKDIR /app

# Copy all project files
COPY . /app

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Set default command
CMD ["python3", "app.py"]





#FROM python:3.10-slim-buster

#RUN apt update -y && apt install awscli -y
#WORKDIR /app

#COPY . /app
#RUN pip install -r requirements.txt

#CMD ["python3", "app.py"]