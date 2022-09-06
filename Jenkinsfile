pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('prueba') {
            steps {
                sh 'python3 prueba.py'
          }
       }
    }
}

