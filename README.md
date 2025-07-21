# Chicken_Disease_Classification


## How to Run

### Step 1:Clone the Repository

```bash
https://github.com/
```

### Step 2: Create a conda Environment after opening the repository

```bash
conda create -n cnncls python=3.10 -y
```

```bash
conda activate cnncls
```


### Step 3: Install the Requirements
```bash
pip install -r requirements.txt
```


## Entire Workflows

1. Update config.yaml file
2. Update params.yaml
3. Update entity
4. Update Configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the app.py



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.
## 2. Create IAM user for deployment

#with specific access

1. EC2 access : It is virtual machine

2. ECR: Elastic Container registry to save your docker image in aws


#Description: About the deployment

1. Build docker image of the source code

2. Push your docker image to ECR

3. Launch Your EC2 

4. Pull Your image from ECR in EC2

5. Lauch your docker image in EC2

#Policy:

1. AmazonEC2ContainerRegistryFullAccess

2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image

- Save the URI: 796586191671.dkr.ecr.ap-south-1.amazonaws.com/dlproj

## 4. Create EC2 machine (Ubuntu)
## 5. Open EC2 and Install docker in EC2 Machine:

#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

## 6. Configure EC2 as self-hosted runner:

setting>actions>runner>new self hosted runner> choose os> then run command one by one

## 7. Setup github secrets:

AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = ap-south-1

AWS_ECR_LOGIN_URI = 796586191671.dkr.ecr.ap-south-1.amazonaws.com/dlproj

ECR_REPOSITORY_NAME = dlproj


# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:



## Run from terminal:








## Deployment Steps:
1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure
4. Pull the Docker image from the container registry to Web App server and run