pipeline {
  agent any
  stages {
    stage('Test'){
      agent{
        docker{
          image 'roretar/python_converter:unittest'
        }
      }
      environment {
        PYTHONPATH = "${WORKSPACE}/CONVERTER"
      }            
      steps {
        sh 'pytest -v --html=rep.html --show-capture=all ${WORKSPACE}/'
      }
      post {
        always {
          archiveArtifacts artifacts: 'rep.html', fingerprint: true
        }
    }}
    stage('Code Inspection'){
      steps {
        sh 'echo Code inspection stage'
      }
    }
    stage('Deploy'){
      steps {
        sh 'echo Deploy'
      }
    }
  }
}