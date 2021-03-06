pipeline {
    agent any
    environment {
        AWS_ACCOUNT_ID="573847103844"
        AWS_DEFAULT_REGION="ap-south-1"
        IMAGE_REPO_NAME="demo-app"
        IMAGE_TAG="latest"
        REPOSITORY_URI="${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
        INVENTORY_FILE="/ansible_data/inventory/demo_app_inventory.ini"
    }

    stages {
        stage('ECR_Login'){
             steps {
                script {
                    sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                }
            }
        }

        stage('Build') {
            steps {
                dir("demo-app") {
                    script {
                        dockerImage = docker.build "${IMAGE_REPO_NAME}:${IMAGE_TAG}"
                    }
                }
            }
        }
        stage('Push to ECR') {
            steps {
                script {
                    sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
                    sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
                }
            }
        }
        stage('Deploy') {
            steps {
                ansiblePlaybook credentialsId: 'app_host', disableHostKeyChecking: true, installation: '/usr/bin/ansible', inventory: "${INVENTORY_FILE}", playbook: 'playbooks/app_deploy.yaml'
            }
        }
    }
}