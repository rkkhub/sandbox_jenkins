pipeline {
//   agent any
  agent { label 'default-agent' }


  environment {
    // image name + unique tag per build
    IMAGE_NAME = "fastapi-hello:${env.BUILD_NUMBER}"
  }

  options {
    // keep only the last 10 builds
    buildDiscarder(logRotator(numToKeepStr: '10'))
}
  stages {
    stage('Checkout') {
      steps {
        // pull main branch
        git branch: 'main',
            url: 'https://github.com/rkkhub/sandbox_jenkins.git'
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          // uses Docker socket mounted into Jenkins
          docker.build(env.IMAGE_NAME, '.')
        }
      }
    }

    stage('Test') {
      steps {
        script {
          // create a folder for test reports
          sh 'pwd'
          sh 'mkdir -p reports'
          sh 'pwd && ls -l'
        //   sh 'ls -l ./workspace/reports'
          // run pytest inside the new image, generate JUnit XML
          docker.image(env.IMAGE_NAME).inside('--entrypoint=') {
            sh 'pwd && ls -l'
            sh 'pytest --junitxml=reports/junit.xml'
          }
          // now list from the host’s POV
          sh 'ls -R reports'

        }
      }
    }
    stage('Cleanup') {
        steps {
            script {
            sh "docker rmi -f ${env.IMAGE_NAME} || true"
            }
        }
    }} // stages
  post {
    always {
        // archive & display test results in Jenkins
        // match one file…
        junit 'reports/junit.xml'
        archiveArtifacts artifacts: 'reports/junit.xml', fingerprint: true, allowEmptyArchive: true
    }
  }
}