pipeline {
    agent any

    environment {
        DOCKER_CREDENTIALS_ID = 'dockerhub' // Jenkins credentials ID
        IMAGE_NAME = 'keerthins123/my-python-app:latest' // Replace with your Docker Hub username
    }

    stages {
        stage('Git checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/keerthi-ns/DeployAppUsingKubernetes.git']])
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh 'docker build -t ${IMAGE_NAME} .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Login to Docker Hub
                    withDockerRegistry(credentialsId: '2969c022-3f74-4d87-a3c9-02cd3a2cfef9', toolName: 'docker') {
                        echo 'Logged in to Docker Hub'
                        sh 'docker push ${IMAGE_NAME}'
                    }
                }
            }
        }

        
        stage('Deploy') {
            steps {
                script {
                    // Run the Docker container in the background
                    sh 'docker run -d -p 5000:5000 --name my-python-app ${IMAGE_NAME}'
                }
            }
        }
    }

    post {
        success {
            echo 'Deployment successful!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
