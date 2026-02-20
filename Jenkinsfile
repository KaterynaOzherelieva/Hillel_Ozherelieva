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
                bat '''
                    python -m venv .venv
                    .venv\\Scripts\\pip install --upgrade pip
                    .venv\\Scripts\\pip install -r requirements.txt
                '''
            }
        }

        stage('Start Flask') {
            steps {
                bat '''
                    start /B .venv\\Scripts\\python homework_lesson_24\\cars_app.py > flask.log 2>&1
                    timeout /t 5
                '''
            }
        }

        stage('Run tests') {
            steps {
                bat '''
                    .venv\\Scripts\\python -m pytest homework_lesson_24\\tests_cars_api_search --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            bat '''
                taskkill /F /IM python.exe || exit 0
            '''
            allure includeProperties: false,
                   jdk: '',
                   commandline: 'allure',
                   results: [[path: 'allure-results']]
        }
    }
}