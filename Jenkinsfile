pipeline {
  agent any
  stages {
    stage('Test'){
      agent{
        docker{
          image 'roretar/python_converter:1.0'
        }
      }
      environment {
        PYTHONPATH = "/var/jenkins_home/workspace/task4_task4@2/CONVERTER"
      }            
      steps {
        sh 'pwd'
        sh 'ls -la'
        sh 'pytest --cov=CONVERTER/src/com/jalasoft/converter/model'
      }
    }
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