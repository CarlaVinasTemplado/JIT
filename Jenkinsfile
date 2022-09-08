pipeline {
    agent any
    parameters {
        text(name: 'parameters', description:'Introduce el código de las incidencias en curso de la JIT anterior.', defaultValue:'')
    }
    stages {
        stage('Upload needed file'){
            steps{
                script {
                    echo 'Upload a zip file with excel Incidencias and parameters'

                    def inputFile = input message: 'Inserta el excel de incidencias actualizado', parameters: [file(name: 'inc_file')]
                    writeFile(file: 'inc_file.xlsx', encoding: 'Base64', text: inputFile.read().getBytes().encodeBase64().toString())
                }
            }
     
        stage('Run generator') {
            steps {
                sh '''
                        #!/bin/bash
                            export PYTHONPATH=$PWD
                        #We make our virtual environment
                        /opt/rh/rh-python36/root/usr/bin/python -m venv .env
                source .env/bin/activate
                
                python task.py $parameters
                python archivo.py '''
                
                archiveArtifacts artifacts: '/output/*', followSymlinks: false
            }
        }
     }
        post {
            always{
                cleanWs()
            }
        }
}

