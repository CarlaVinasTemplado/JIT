pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python --version'
            }
        }
        stage('prueba') {
            steps {
                sh 'python prueba.py'
          }
       }
    }
}

