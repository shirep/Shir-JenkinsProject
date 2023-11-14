pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }

        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                    sh 'pip3 install pylint'
                }
            }
        }

        stage('Lint') {
            steps {
                script {
                    sh 'pylint app.py'
                }
            }
        }

        stage('Docker Build') {
            steps {
                script {
                    sh 'docker build -t shir-python-image .'
                }
            }
        }

        stage('Publish Docker Image') {
            steps {
                script {
                    sh 'docker push shir-python-image'
                }
            }
        }
    }

    post {
        success {
            echo 'Success'
        }
        failure {
            echo 'Failed'
        }
    }
}
