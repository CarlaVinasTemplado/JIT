pipeline {
    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('Execution') {
            steps {
                sh 'python3 task.py'
          }
       }
    }
}

