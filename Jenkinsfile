pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/aioticstraining/chatbot-demo.git'
            }
        }
         stage('Run Tests') {
            steps {
                // Run your tests
                sh 'pytest'
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
