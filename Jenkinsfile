pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo "Checking out source code"
                checkout scm
            }
        }
        stage('Test') {
            steps {
                echo "testing applications"
                sh 'python3 -m unittest discover -v'
            }
        }
        stage('Package') {
            steps {
                echo"Building application"
                sh 'zip -r "hello-app-v${BUILD_NUMBER}.zip" *.py'
                archiveArtifacts 'hello-app-v*.zip'
            }
        }
    }
    post {
        success { echo 'CI/CD WORKS!' }
        failure { echo 'Fix the code!' }
    }
}
