pipeline {
    agent any

    environment {
        DOCKERHUB_USERNAME = "samithaagrapala"
        DOCKERHUB_PASSWORD = "Samitha@0509"
        BACKEND_IMAGE = "samithaagrapala/car-rent-backend:1.0"
        FRONTEND_IMAGE = "samithaagrapala/car-rent-frontend:1.0"
    }

    stages {

        stage('Build Backend Image') {
            steps {
                sh 'docker build -t $BACKEND_IMAGE ./be'
            }
        }

        stage('Build Frontend Image') {
            steps {
                sh 'docker build -t $FRONTEND_IMAGE ./fe'
            }
        }

        stage('Docker Login & Push') {
            steps {
                sh '''
                echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin
                docker push $BACKEND_IMAGE
                docker push $FRONTEND_IMAGE
                '''
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/mongo.yaml
                kubectl apply -f k8s/backend.yaml
                kubectl apply -f k8s/frontend.yaml
                '''
            }
        }
    }

    post {
       success {
           echo 'Deployment Successful!'
       }
       failure {
           echo 'Deployment Failed!'
        }
        always {
           cleanWs()
        }
    }
}
