pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                bat 'python3 --version'
            }
        }
        stage('prueba') {
            steps {
                bat 'python3 task.py'
          }
        }
    }      
}
