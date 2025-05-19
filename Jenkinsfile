pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Nahelawad/CICD-project.git'
            }
        }

        stage('Install Dependencies & Test') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'python -m unittest test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t todo-app .'
            }
        }

        stage('Deploy App') {
            steps {
                bat 'docker stop todo-container || exit 0'
                bat 'docker rm todo-container || exit 0'
                bat 'docker run -d -p 5000:5000 --name todo-container todo-app'
            }
        }
    }
}
