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

        # Remove dangling containers occupying the port
        existing_container=$(docker ps -q --filter "publish=5000")
        if [ ! -z "$existing_container" ]; then
            echo "Found container using port 5000. Stopping and removing it..."
            docker stop $existing_container
            docker rm $existing_container
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
