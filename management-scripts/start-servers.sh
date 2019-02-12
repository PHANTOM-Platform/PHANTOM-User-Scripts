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
	echo "##### Starting Repository..."
	echo "##################################################"
	cd $REPO_DIR
	bash start-repo.sh

	echo "##################################################"
	echo "##### Starting APP Manager..."
	echo "##################################################"
	cd $APPM_DIR
	bash start-appmanager.sh

	echo "##################################################"
	echo "##### Starting Execution Manager..."
	echo "##################################################"
	cd $EXE_DIR
	bash start-execmanager.sh

	echo "##################################################"
	echo "##### Starting Resource Manager..."
	echo "##################################################"
	cd $RES_DIR
	bash start-resomanager.sh

	echo "##################################################"
	echo "##### Starting Monitoring Server..."
	echo "##################################################"
	cd $MON_DIR
	bash start-monitoring-server.sh













