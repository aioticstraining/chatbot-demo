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
                    sonar-scanner \
                        -Dsonar.login=squ_0df74914a393bdb6b73014e5480772839b92697c \
                        -Dsonar.projectKey=chatbot-demo \
                        -Dsonar.projectName=Chatbot Demo \
                        -Dsonar.projectVersion=1.0 \
                        -Dsonar.sources=.
                    '''
                }
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
