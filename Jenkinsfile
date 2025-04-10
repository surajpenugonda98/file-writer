pipeline {
    agent any

    parameters {
        string(name: 'TARGET_DIR', defaultValue: '/workspace/dev-app', description: 'Directory to sync code into')
        string(name: 'GIT_BRANCH', defaultValue: 'master', description: 'Branch to update')
    }

    environment {
        REPO_URL = 'https://github.com/surajpenugonda98/file-writer.git'
    }

    stages {
        stage('Update Code') {
            steps {
                script {
                    if (!fileExists("${params.TARGET_DIR}/.git")) {
                        echo "Directory doesn't exist or is not a Git repo. Cloning fresh."
                        sh "git clone -b ${params.GIT_BRANCH} ${env.REPO_URL} ${params.TARGET_DIR}"
                    } else {
                        echo "Git repo found. Pulling latest changes from branch '${params.GIT_BRANCH}'"
                        dir("${params.TARGET_DIR}") {
                            sh """
                                git checkout ${params.GIT_BRANCH} || git checkout -b ${params.GIT_BRANCH} origin/${params.GIT_BRANCH}
                                git pull origin ${params.GIT_BRANCH}
                            """
                        }
                    }
                }
            }
        }
    }

    post {
        success {
            echo "✅ Repository updated successfully in ${params.TARGET_DIR}"
        }
        failure {
            echo "❌ Failed to update the repository. Please check errors above."
        }
    }
}
