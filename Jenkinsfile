pipeline {
    agent any
    parameters {
        string(name: 'name_inc', defaultValue: 'none', description: 'nombre de la incidencia')
    }
    environment {
        name_final = "{$name_inc}"
    }
    
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
