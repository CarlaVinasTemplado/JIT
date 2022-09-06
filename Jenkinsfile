pipeline {
    agent any
    stages {
        stage('version') {
            steps {
                sh 'python --version'
            }
        }
        stage('Execution') {
            steps {
                sh 'python task.py'
          }
       }
    }
}

