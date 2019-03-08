#!/bin/bash


export PATH=/home/demo/phantom_servers/dist/nodejs:/home/demo/phantom_servers/dist/nodejs/bin:$PATH

# GLOBAL Variables
	THIS_DIR=$(pwd)
	BASE_DIR=${THIS_DIR}/../../
	REPO_DIR=${BASE_DIR}/Repository
	APPM_DIR=${BASE_DIR}/Application-Manager
	EXE_DIR=${BASE_DIR}/Execution-Manager
	RES_DIR=${BASE_DIR}/Resource-Manager
	MON_DIR=${BASE_DIR}/Monitoring/Monitoring_server
	OffMOM_DIR=${BASE_DIR}/OfflineMOM
	USER_DIR=${BASE_DIR}/User-tools
	SERVERS_DIR=/home/demo/phantom_servers/

	

# Stop servers
	bash stop-servers.sh

# Start updates
	printf "\n##################################################\n"	
	printf "##### Updating Repository...\n"
	printf "##################################################\n"
	cd $REPO_DIR &&
	git pull &&
	cp {package.json,package-lock.json} ${SERVERS_DIR}
	cd ${SERVERS_DIR} &&
	npm update


	printf "\n##################################################\n"
	printf "##### Updating APP Manager...\n"
	printf "##################################################\n"
	cd $APPM_DIR &&
	git pull
	
	printf "\n##################################################\n"
	printf "##### Updating Execution Manager...\n"
	printf "##################################################\n"
	cd $EXE_DIR &&
	git pull
	
	printf "\n##################################################\n"
	printf "##### Updating Resource Manager...\n"
	printf "##################################################\n"
	cd $RES_DIR &&
	git pull
	
	printf "\n##################################################\n"
	printf "##### Updating OfflineMOM...\n"
	printf "##################################################\n"
	cd $OffMOM_DIR &&
	git pull

	printf "\n##################################################\n"
	printf "##### Updating User-tools...\n"
	printf "##################################################\n"
	cd $USER_DIR  &&
	git pull

# Start servers
	cd ${THIS_DIR} &&
	bash start-servers.sh



	


