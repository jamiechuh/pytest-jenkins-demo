pipeline {
    agent any // 在任意可用节点上执行

    stages {
        stage('Checkout') {
            steps {
                // Jenkins 会自动根据上面的 SCM 配置拉取代码
                echo '代码拉取完成'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // --junitxml 让 pytest 生成 JUnit 格式的报告
                sh 'pytest tests/ --junitxml=reports/results.xml'
            }
        }
    }

    post {
        always {
            // 无论测试成功还是失败，都收集报告
            junit 'reports/results.xml'
        }
    }
}
