pipeline {
    agent any

    environment {
        VENV_DIR = '.venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Kashishoza/PRACTICE.git'
            }   
        }

        stage('Setup Virtual Environment') {
            steps{
                sh ''' 
                    python3 -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source ${VENV_DIR}/bin/activate
                    pytest
                '''
            }
        }

    }

    post {
        success {
            echo 'All tests Passed'
        }
        failure {
            echo 'Test Failed'
        }
    }


}