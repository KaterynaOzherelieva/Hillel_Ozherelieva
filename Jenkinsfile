pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/KaterynaOzherelieva/Hillel_Ozherelieva.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    ./.venv/bin/python -m pip install --upgrade pip
                    ./.venv/bin/python -m pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    ./.venv/bin/python -m pytest Tests/test_homework_12.py --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false,
                   commandline: 'allure',
                   results: [[path: 'allure-results']]
        }
    }
}
