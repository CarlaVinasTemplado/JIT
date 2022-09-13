pipeline {

    agent {

              docker {

                args '--network=host'

                image 'docker-python-36'

                label 'paqfaast09'

              }

     }

 

    parameters {

        extendedChoice bindings: '', description: 'needed json parameters', groovyClasspath: '', groovyScript: ''' import net.sf.json.JSONObject

 

def jsonEditorOptions = JSONObject.fromObject(/{

        disable_edit_json: true,

        disable_properties: true,

        no_additional_properties: true,

        disable_collapse: true,

        disable_array_add: false,

        disable_array_delete: false,

        disable_array_reorder: true,

        theme: "bootstrap3",

        use_default_values:true,

 

        iconlib:"spectre",

        schema: {

          "type": "object",

          "title": "Input for release",

          "properties": {

    "Incidencias": {

      "type": "array",

      "format":"table",

      "items":

        {

          "type": "object",

          "properties": {

            "codigo": {

              "type": "string"  }

            }

        }

    }

    }

        },

}/); ''', multiSelectDelimiter: ',', name: 'jsop', quoteValue: false, saveJSONParameterToFile: true, type: 'PT_JSON', visibleItemCount: 5

     }

 

 

 

    stages {

        stage('Parameters To Json') {

            steps {

                sh "printenv jsop > input_file.json"

                archiveArtifacts artifacts: '*.json', followSymlinks: false

 

            }

        }

 

 

       

        stage('Upload needed files') {

            steps {

                 script{

               

                    def inputFile = input message: 'Inserte el excel de incidencias.', parameters: [file(name: 'input')]

                                                                               writeFile(file: 'input_excel.xlsx',encoding: 'Base64', text: inputFile.read().getBytes().encodeBase64().toString())

                                                               }

            }

       }

 

        stage('Run generator') {

            steps {

 

                sh '''

                                    #!/bin/bash

                                                                               export PYTHONPATH=$PWD

                                    # We make our virtual environment

                                    /opt/rh/rh-python36/root/usr/bin/python -m venv .env

                        source .env/bin/activate

 

                       

                        python --version

                       

                        #pip install dependencies/python-docx-0.8.10.tar.gz

                        #pip install dependencies/pandas-1.4.4.tar.gz

                        #pip install dependencies/XlsxWriter-1.3.0.tar.gz

 

 

                        python JIT/prueba.py input_file.json input_excel.xlsx --verbose 10

 

 

 

 

                                    '''

                                    archiveArtifacts artifacts: '*', followSymlinks: false

 

 

 

            }

        }

    }

          post {

            always {

              cleanWs()

 

            }

      }

}
