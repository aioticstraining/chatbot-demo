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
        stage('SonarQube Analysis') {
            steps {
                sh 'sonar-scanner -Dsonar.projectKey=Chatbot -Dsonar.sources=.'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t chatbot-app:latest .'
            }
        }
        stage('Push to Artifactory') {
            steps {
                sh 'docker tag chatbot-app:latest <artifactory-url>/chatbot-app:latest'
                sh 'docker push <artifactory-url>/chatbot-app:latest'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 chatbot-app:latest'
            }
        }
    }
}
