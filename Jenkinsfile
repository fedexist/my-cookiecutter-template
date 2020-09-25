pipeline {
    agent any

    environment {
        PROJECT_ID = 'poc-generali-aal'
        LOCATION = 'europe-west1-b'
        CREDENTIALS_ID = 'jenkins-service-account'
    }

    stages {

        stage('Clone sources') {
            steps {
                slackSend (color: '#FFFF00', message: "STARTED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
                checkout scm
            }
        }

        /*
        stage('Run tests') {
            environment {
                ENV='TEST'
            }
            steps {
                sh '''
                python3.8 -m venv venv
                . venv/bin/activate
                python3.8 -m pip install pip tox --upgrade
                python3.8 -m tox
                '''
            }
        }*/

        stage('Generate and publish doc') {
            steps {
                withCredentials([string(credentialsId: 'confluence-token', variable: 'CONFLUENCE_TOKEN')]) {
                    sh '''
                    cd docs
                    make confluence
                    '''
                }
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