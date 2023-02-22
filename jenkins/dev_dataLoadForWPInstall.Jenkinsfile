pipeline {
    agent any
    environment {
        FAILURE_DISTRO = 'amir.khan@team.neustar'
        SUCCESS_DISTRO = 'amir.khan@team.neustar'
        DEV_USER_NAME_PASS=credentials('DEV_USER_NAME_PASS')
        DEV_USER_NAME="${DEV_USER_NAME_PASS_USR}"
        DEV_PASSWORD="${DEV_USER_NAME_PASS_PSW}"
        DEV_HOST_NAME='wpinstall.cv8szn5hkhmy.ap-south-1.rds.amazonaws.com'
        DEV_DATABASE_NAME='wp_install'
        DEV_TABLE_NAME_BUS='full_usbus'
        DEV_TABLE_NAME_RES='full_usres'
        DEV_FILE_NAME_BUS='full_usbus.sql'
        DEV_FILE_NAME_RES='full_usres.sql'

    }
    options {
        skipDefaultCheckout()
        skipStagesAfterUnstable()
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jenkinstesting0123/wpinstall.git']])
                 
                }
            }
         // End of Checkout stage
        stage('DataDump') {
            parallel {
                stage("Dump_full_usbus"){
                    steps {
                      script {
                            try {
                                sh ' python wpinstall-sync.py -u ${DEV_USER_NAME} -p ${DEV_PASSWORD} -h ${DEV_HOST_NAME} -d ${DEV_DATABASE_NAME} -t ${DEV_TABLE_NAME_BUS} -f ${DEV_FILE_NAME_BUS} --datadump'
                                /*bat """python wpinstall-sync.py -u ${DEV_USER_NAME} -p ${DEV_PASSWORD} -h ${DEV_HOST_NAME} -d ${DEV_DATABASE_NAME} -t ${DEV_TABLE_NAME_BUS} -f ${DEV_FILE_NAME_BUS} --datadump""" */
                            }
                            catch(Exception e) {
                                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE')
                                error('Error In stage DataDump_usbus')
                            }
                        }
                    }

                }
                stage("Dump_full_usres"){
                    steps {
                        script {
                            try {
                                sh ' python3 hello.py'
                                /*bat """python wpinstall-sync.py -u ${DEV_USER_NAME} -p ${DEV_PASSWORD} -h ${DEV_HOST_NAME} -d ${DEV_DATABASE_NAME} -t ${DEV_TABLE_NAME_RES} -f ${DEV_FILE_NAME_RES} --datadump""" */
                            }
                            catch(Exception e) {
                                catchError(buildResult: 'UNSTABLE', stageResult: 'FAILURE')
                                error('Error In stage DataDump_usres')
                            }
                        }
                    }
                
                }
            }
        }
        stage('DataLoad') {
            parallel {
                stage('DataLoad_BUS') { 
                    steps {
                        sh ' python3 hello.py'
                        /*bat """python wpinstall-sync.py -u ${DEV_USER_NAME} -p ${DEV_PASSWORD} -h ${DEV_HOST_NAME} -d ${DEV_DATABASE_NAME} -f ${DEV_FILE_NAME_BUS} --loaddata"""*/
                    }
                }
                stage('DataLoad_RES') {
                    steps {
                        sh ' python3 hello.py'
                        /*bat """python wpinstall-sync.py -u ${DEV_USER_NAME} -p ${DEV_PASSWORD} -h ${DEV_HOST_NAME} -d ${DEV_DATABASE_NAME}  -f ${DEV_FILE_NAME_RES} --loaddata"""*/
                    }
                }
            }
        }
        stage('Removingdumpfile') {
            steps {
                script {
                    try {
                        sh ' python3 hello.py'
                       /*bat """del .sql"""*/
                    }
                    catch(Exception e) {
                        error('Error In stage RemovingSidiousWPCADUMP')
                    }
                }
            }
        } 
    }
    /*post {
        success {
            mail body: "<b>CR Data Capture -- YPCRInstall Data Load</b><br>\\n\\<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}", 
            charset: 'UTF-8', 
            from: 'no-reply@team.neustar', 
            mimeType: 'text/html',  
            replyTo: '',  
            subject: "SUCCESS Data Load -> ${env.JOB_NAME}", 
            to: "${SUCCESS_DISTRO}"
            bat 'delete-dump-file.bat'
        }
        failure { 
            mail body: "<b>CR Data Capture -- YPCRInstall Data Load</b><br>\\n\\<br>Project: ${env.JOB_NAME} <br>Build Number: ${env.BUILD_NUMBER} <br> URL de build: ${env.BUILD_URL}",
            charset: 'UTF-8', 
            from: 'no-reply@team.neustar', 
            mimeType: 'text/html',  
            replyTo: '',  
            subject: "FAILURE Data Load -> ${env.JOB_NAME}",
            to: "${FAILURE_DISTRO}"
        }         
    } */
}
