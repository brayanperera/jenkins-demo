pipeline {
    agent any
    environment {
        registry = "demo-app:latest 363052508649.dkr.ecr.ap-southeast-1.amazonaws.com/demo-app"
    }
    stages {
        stage('Build') {
            steps {
                script {
                    echo 'Building demo-app'; cd demo_app
                    docker build -t "demo-app:latest" .
                    docker tag "demo-app:latest 363052508649.dkr.ecr.ap-southeast-1.amazonaws.com/demo-app:latest"
                    docker push "363052508649.dkr.ecr.ap-southeast-1.amazonaws.com/demo-app:latest"
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}