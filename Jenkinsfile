pipeline {
    node {
        timeout(time: 5, unit: "MINUTES") {
            INPUT_PARAMS = input(
                message: 'Please provide the parameter input:',
                ok: 'Next',
                parameters: [
                    booleanParam(defaultValue: true, name: 'Create Jira Tickets?', description: ''),
                    booleanParam(defaultValue: true, name: 'Encrypted?', description: 'Use for secrets/passwords/certificates/etc'),
                    multipleChoice(name: 'Environments', choices: ["prod", "eu", "test", "mgmt"], description: 'Environments to create parameter in'),
                    string(name: 'Path', description: 'SSM Parameter Path'),
                    text(name: 'Value', description: 'Parameter Value')
                ]
            )
        }
    }


    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('prueba') {
            steps {
                sh 'python3 task.py'
          }
       }
    }
}

