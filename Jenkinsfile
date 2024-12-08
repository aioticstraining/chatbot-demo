pipeline {
    agent {
        node {
            label 'chatbot'
        }
    }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/aioticstraining/chatbot-demo.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t chatbot-app:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 chatbot-app:latest'
            }
        }
    }
}
