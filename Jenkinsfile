pipeline {
    agent any
    environment {
        BRANCH_NAME = "${env.BRANCH_NAME}" // Jenkins environment variable for branch name
    }
    stages {
        stage('Clone Repository') {
            steps {
                checkout scm // Checkout the branch triggering the build
            }
        }
        stage('SonarQube Analysis') {
            when {
                branch 'master'
            }
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
                sh 'docker build -t chatbot-app:${BRANCH_NAME} .'
            }
        }
        stage('Clean Up Existing Container') {
            when {
                branch 'master'
            }
            steps {
                sh '''
                if docker ps --filter "name=chatbot-app" --format "{{.ID}}" | grep -q .; then
                    docker stop chatbot-app
                    docker rm chatbot-app
                fi

                existing_container=$(docker ps -q --filter "publish=5000")
                if [ ! -z "$existing_container" ]; then
                    docker stop $existing_container
                    docker rm $existing_container
                fi
                '''
            }
        }
        stage('Deploy') {
            when {
                branch 'master'
            }
            steps {
                sh '''
                docker run -d --name chatbot-app -p 5000:5000 chatbot-app:${BRANCH_NAME}
                '''
            }
        }
    }
}
