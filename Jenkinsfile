pipeline {
  agent { label 'docker' }
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  triggers {
    cron('@daily')
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -f "tallapaneni/ramudev" -t tallapaneni/ramudev:${select_commit} .'
      }
    }
    stage('Publish') {
      when {
        branch 'test'
      }
      steps {
        withDockerRegistry([ credentialsId: "'a6ac2b26-ad40-4aa9-ae50-726e50b55f42'", url: "https://index.docker.io/v1/" ]) {
          sh 'tallapaneni/ramudev:${select_commit}'
        }
      }
    }
  }
}
