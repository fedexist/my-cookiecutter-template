pipeline {
    agent any

    stages {

        stage('Clone sources') {
            steps {
                slackSend (color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
                checkout scm
            }
        }


        stage('Setup venv') {
            environment {
                ENV='TEST'
            }
            steps {
                sh '''
                python3.8 -m venv venv
                . venv/bin/activate
                python3.8 -m pip install pip tox --upgrade
                python3.8 -m pip install -r requirements_dev.txt
                '''
            }
        }
    }

    post {
        always {
            cleanWs deleteDirs: true, disableDeferredWipeout: true, patterns: [[pattern: '', type: 'INCLUDE']]
        }
        success {
            slackSend (color: '#00FF00', message: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
        }
        failure {
            slackSend (color: '#FF0000', message: "FAILURE: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")

        }
    }
}
