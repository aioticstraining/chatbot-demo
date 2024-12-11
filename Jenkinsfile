pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/aioticstraining/chatbot-demo.git'
            }
        }
        stage('SonarQube Analysis') {
            steps {
              withSonarQubeEnv('SonarQube Server') {
                    sh '''
                sonar-scanner -Dsonar.login=$SONAR_TOKEN
                    '''
}            }
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
