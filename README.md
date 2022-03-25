# jenkins-demo

## Overview

This project deploy Jenkins server on AWS 

## Architecture

## Infrastructure Preparation

### AWS Infrastructure setup via Cloudformation

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




## Application Usage

### Dev Environment (Local)

### Prod Environment 