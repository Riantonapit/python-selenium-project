pipeline {
    agent {
        docker {
            image 'python:3.10'
            args '-u root' // agar bisa install dependensi jika perlu
        }
    }
    environment {
        PIP_DISABLE_PIP_VERSION_CHECK = '1'
        PYTHONDONTWRITEBYTECODE = '1'
    }
    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/Riantonapit/python-selenium-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
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
