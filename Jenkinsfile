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
        stage('Clean Up Existing Container') {
            steps {
                sh '''
                # Stop and remove any running container with the name chatbot-app
                if docker ps --filter "name=chatbot-app" --format "{{.ID}}" | grep -q .; then
                    docker stop chatbot-app
                    docker rm chatbot-app
                fi

                # Ensure port 5000 is free
                if lsof -i:5000 | grep -q LISTEN; then
                    echo "Port 5000 is in use. Cleaning up..."
                    fuser -k 5000/tcp
                fi
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d -p 5000:5000 chatbot-app:latest'
            }
        }
    }
}
