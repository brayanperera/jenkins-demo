# jenkins-demo

## Overview

This project deploy Jenkins server on AWS 

## Architecture

[Detailed Presentation](docs/Jenkins-Demo-BrayanPerera.pptx)

## Infrastructure Preparation

Infrastructure preparation has two stages

- AWS Infrastructure setup via Cloudformation
- Post Instance creation steps
  - Jenkins Initial configurations
  - App host deployment env setup


### AWS Infrastructure setup via Cloudformation

#### Pre-Requisites 

Following items should be available in the AWS account / region

- IAM User
  - 
- EC2 Keypair

For CLI based cloudformation stack creation. 
- VM/PC with aws cli installed

#### Stack creation via CLI

1. Source your AWS credential in the client PC/VM

**Note:** Fill the values accordingly 

```bash
export AWS_ACC_NUMBER=""
export AWS_USERNAME=""
export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_DEFAULT_REGION=""
```

2. Execute create stack

```bash

cd <path_of_the_jenkins-demo>
aws cloudformation create-stack --capabilities CAPABILITY_NAMED_IAM --stack-name demo-stack \
--template-body file://infra_provisioning//jenkins_infra.yaml
```



### Application Deployment to App server instance

Application deployment should happen via Jenkins pipeline utilizing Ansible Playbook. 

Playbook steps:

- Upload docker-compose.yaml to the App Host. 
- Perform `docker-compose up` to re-create the new container
- Perform post-deploy scripts
  - DB migration

#### Initial Manual Steps

- Upload sqlite db file
  - Path: ``
- Upload access ssh key to Jenkins server


### Jenkins Init Configs

#### Required Plugins

- Amazon ECR plugin Version1.7
- Ansible plugin Version1.1
- Docker Pipeline Version1.28
- Docker plugin Version1.2.6

### Pipeline Job Creation

- In GitHub create a webhook towards Jenkins
- In Jenkins
  - New Items 
    - Name: "Demo-App-Pipeline"
    - Type: Pipeline
  - In `General` Section
    - Select `GitHub project`
    - Enter project URL 
      - https://github.com/brayanperera/jenkins-demo
  - In `Build Triggers`
    - Select `GitHub hook trigger for GITScm polling`
  - In `Pipeline`
    - Repository URL
      - https://github.com/brayanperera/jenkins-demo.git
    - Branch Specifier
      - */main
  - Script Path
    - Jenkinsfile
    

## Application startup 

````bash
cd /home/ec2-user/apps/demo_app
docker-compose up -d
````
