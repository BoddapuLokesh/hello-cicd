pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -v'
            }
        }
        stage('Package') {
            steps {
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
