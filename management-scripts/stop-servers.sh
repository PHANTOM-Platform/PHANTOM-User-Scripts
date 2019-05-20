#!/bin/bash

# GLOBAL Variables
BASE_DIR=$(pwd)/../../
REPO_DIR=${BASE_DIR}/Repository
APPM_DIR=${BASE_DIR}/Application-Manager
EXE_DIR=${BASE_DIR}/Execution-Manager
RES_DIR=${BASE_DIR}/Resource-Manager
MON_DIR=${BASE_DIR}/Monitoring/Monitoring_server




# Start servers
echo "##################################################"	
echo "##### Stopping Repository..."
echo "##################################################"
cd $REPO_DIR
bash stop-repo.sh

echo "##################################################"
echo "##### Stopping APP Manager..."
echo "##################################################"
cd $APPM_DIR
bash stop-appmanager.sh

echo "##################################################"
echo "##### Stopping Execution Manager..."
echo "##################################################"
cd $EXE_DIR
bash stop-execmanager.sh

echo "##################################################"
echo "##### Stopping Resource Manager..."
echo "##################################################"
cd $RES_DIR
bash stop-resomanager.sh

echo "##################################################"
echo "##### Stopping Monitoring Server..."
echo "##################################################"
cd $MON_DIR
bash stop-monitoring-server.sh













