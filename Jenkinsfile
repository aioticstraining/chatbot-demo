pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/aioticstraining/chatbot-demo.git'
            }
        }
    stage('SonarQube Analysis') {
            def scannerHome = tool 'SonarScanner';
            withSonarQubeEnv() {
              sh "${scannerHome}/bin/sonar-scanner"
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
