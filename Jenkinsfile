pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/Riantonapit/python-selenium-project.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
    }
}
