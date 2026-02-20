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

        stage('Start Flask') {
            steps {
                sh '''
                    snohup ./.venv/bin/python homework_lesson_24/cars_app.py > flask.log 2>&1 &
                    sleep 5
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    ./.venv/bin/python -m pytest homework_lesson_24/tests_cars_api_search --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            sh 'pkill -f "homework_lesson_24/cars_app.py" || true'

            allure includeProperties: false,
                   commandline: 'allure',
                   results: [[path: 'allure-results']]
        }
    }
}