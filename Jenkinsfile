pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                bat 'python --version'
            }
        }
        stage('prueba') {
            steps {
                bat 'python task.py'
          }
        }
    }      
}
