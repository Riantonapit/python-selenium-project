pipeline {
    agent any

    environment {
        IMAGE_NAME = 'selenium-python-test'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/USERNAME/python-selenium-project.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t $IMAGE_NAME ."
                }
            }
        }

        stage('Run Tests in Docker') {
            steps {
                script {
                    sh "docker run --rm $IMAGE_NAME"
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline selesai dijalankan.'
        }
        failure {
            echo 'Pipeline gagal.'
        }
    }
}