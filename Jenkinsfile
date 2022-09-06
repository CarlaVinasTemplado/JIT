pipeline {
    agent any
    parameters {
        extendedChoice bindings: '', description: 'needed json parameters', groovyClasspath: '', groovyScript: '''import net.sf.json.JSONObject

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
    "product": {
      "type": "string"
    },
    "version": {
      "type": "object",
      "properties": {
        "fabricante": {
          "type": "string",
        },
        "paquete": {
          "type": "string"
        }
      },
      "required": [
        "fabricante",
        "paquete"
      ]
    },
    "SR": {
      "type": "string"
    },
    "product_owner": {
      "type": "array",
      "format":"table",
      "items":
        {
          "type": "object",
          "properties": {
            "name": {
              "type": "string"
            },
            "email": {
              "type": "string"
            }
          },
          "required": [
            "name",
            "email"
          ]
        }

    },
    "cc": {
      "type": "array",
      "items":
        {
          "type": "string"
        }
    },
    "my_email": {
      "type": "string"
    },
    "my_name": {
      "type": "string"
    },
    "attach": {
      "type": "object",
      "properties": {
        "changelog": {
          "type": "string",
          "enum": ["changelog.md"]
        },
        "security_files_path": {
          "type": "string",
           "enum": ["security_files"]
        },
        "qualys_and_temscan_path": {
          "type": "string",
          "enum": ["qualtem"]
        }
      },
      "required": [
        "changelog",
        "security_files_path",
        "qualys_and_temscan_path"
      ]
    },

    "linea_base": {
      "type": "object",
      "format":"grid",
      "properties": {
        "name": {
          "type": "string",

        },
        "option": {
          "type": "object",
          "properties": {
            "add": {
              "type": "boolean",
               "format": "checkbox"

            },
            "delete": {
              "type": "boolean",
               "format": "checkbox"
            },
            "keep": {
              "type": "boolean",
               "format": "checkbox"
            }
          },
          "required": [
            "add",
            "delete",
            "keep"
          ]
        }
      },
      "required": [
        "name",
        "option"
      ]
    },
    "arquitectura": {
      "type": "object",
      "format":"grid",
      "properties": {
        "32": {
          "type": "boolean",
          "format": "checkbox",
          "default": true

        },
        "64": {
          "type": "boolean",
           "format": "checkbox",
           "default": true

        }
      },
      "required": [
        "32",
        "64"
      ]
    },
    "SO": {
      "type": "object",
      "properties": {
        "windows": {
          "type": "object",
          "format":"grid",
          "properties": {
            "2k3": {
              "type": "boolean",
               "format": "checkbox"
            },
            "2k8": {
              "type": "boolean",
               "format": "checkbox"
            },
            "2k12": {
              "type": "boolean",
               "format": "checkbox"
            },
            "2k12R2": {
              "type": "boolean",
               "format": "checkbox"
            },
            "2k8R2": {
              "type": "boolean",
               "format": "checkbox"
            },
            "2k16": {
              "type": "boolean",
               "format": "checkbox"
            },
            "2k19": {
              "type": "boolean",
               "format": "checkbox"
            }
          },
          "options": {
            "dependencies": {
              "platform": "Windows"
            }
          },
          "required": [
            "2k3",
            "2k8",
            "2k12",
            "2k12R2",
            "2k8R2",
            "2k16",
            "2k19"
          ]
        },
        "linux": {
          "type": "object",
          "format":"grid",
          "options": {
            "dependencies": {
              "platform": "Linux"
            }
          },
          "properties": {
            "RH6": {
              "type": "boolean",
               "format": "checkbox"
            },
            "RH7": {
              "type": "boolean",
               "format": "checkbox"
            },
            "RH8": {
              "type": "boolean",
               "format": "checkbox"
            }
          },
          "required": [
            "RH6",
            "RH7",
            "RH8"
          ]
        }
      },
      "required": [
        "windows",
        "linux"
      ]
    },
    "output_path": {
      "type": "string",
      "enum": ["output"]

    },
    "our_servers": {
      "type": "object",
      "properties": {
        "windows": {
          "type": "object",
          "properties": {
            "2k3": {
              "type": "string",
              "enum": [""]

            },
            "2k8": {
              "type": "string",
              "enum": ["arqowast09.lacaixapre.glcpre.es"]

            },
            "2k8R2": {
              "type": "string",
              "enum": ["arqowast13.lacaixapre.glcpre.es","arqowast15.lacaixapre.glcpre.es"]
            },
            "2k12": {
              "type": "string",
              "enum": ["arqowast17.lacaixapre.glcpre.es"]
            },
            "2k12R2": {
              "type": "string",
              "enum": ["arqowast21.lacaixapre.glcpre.es","arqowast19.lacaixapre.glcpre.es","arqowast23.lacaixapre.glcpre.es"]
            },
            "2k16": {
              "type": "string",
              "enum": ["arqopast21.lacaixapre.glcpre.es","arqopast15.lacaixapre.glcpre.es","arqopast41.lacaixapre.glcpre.es","arqopast43.lacaixapre.glcpre.es"]
            },
            "2k19": {
              "type": "string",
              "enum": ["arqowast03.lacaixapre.glcpre.es"]
            }
          },
          "required": [
            "2k3",
            "2k8",
            "2k8R2",
            "2k12",
            "2k12R2",
            "2k16",
            "2k19"
          ]
        },
        "linux": {
          "type": "object",
          "properties": {
            "RH6": {
              "type": "string",
              "enum": ["paqfaast51.lacaixa.es","arqopwst13.lacaixa.es","arqopast31.lacaixa.es","arqopasr01.lacaixa.es","arqopast13.lacaixa.es"]
            },
            "RH7": {
              "type": "string",
              "enum": ["arqopwst13.lacaixa.es","paqfaast50.lacaixa.es","arqopwst02.lacaixa.es","arqopast17.lacaixa.es","paqfaast01.servicios.loc","arqopast13.lacaixa.es","arqopast19.lacaixa.es","arqopasr21.lacaixa.es","eiproast18.dacfi.es","paqfaast04.servicios.loc","paqfaast06.pe.pr.geos.loc","paqfaast75.dacfi.es","paqfaast76.dacfi.es","paqfaast77.dacfi.es","paqfaast63.lacaixa.es"]
            },
            "RH8": {
              "type": "string",
              "enum": ["arqopwst13.lacaixa.es","arqopwst02.lacaixa.es"]
            }
          },
          "required": [
            "RH6",
            "RH7",
            "RH8"
          ]
        }
      },
      "required": [
        "windows",
        "linux"
      ]
    }
  },
      "security": {
      "type": "object",
      "properties": {
        "catalogo": {
          "type": "string",
          "default":"2020C2_M04"
        },
        "politica": {
          "type": "string",
          "default":"SO"
        },
        "sectype": {
          "type": "string",
          "default":"Gv2019"
        }
      },
      "required": [
        "catalogo",
        "politica",
        "sectype"
      ]
    }
        },
}/);''', multiSelectDelimiter: ',', name: 'json_parameters', quoteValue: false, saveJSONParameterToFile: true, type: 'PT_JSON', visibleItemCount: 5
     }


    stages {
        stage('Parameters To Json') {
            steps {
                sh "printenv json_parameters > input_file.json"
                archiveArtifacts artifacts: '*.json', followSymlinks: false

            }
        }

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
          post {
            always {
              cleanWs()

            }
      }
}

