# jenkins-demo

## Overview

This project deploy Jenkins server on AWS 

## Architecture

## Infrastructure Preparation

### AWS Infrastructure setup via Cloudformation

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


### Application Deployment to App server instance

## Application Usage

### Dev Environment (Local)

### Prod Environment 