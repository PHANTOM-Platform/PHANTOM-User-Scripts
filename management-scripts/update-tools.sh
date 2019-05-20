#!/bin/bash


export PATH=/home/demo/phantom_servers/dist/nodejs:/home/demo/phantom_servers/dist/nodejs/bin:$PATH

# GLOBAL Variables
	THIS_DIR=$(pwd)
	BASE_DIR=${THIS_DIR}/../..
	REPO_DIR=${BASE_DIR}/Repository
	PT_DIR=${BASE_DIR}/Parallelisation-Toolset
	MOM_DIR=${BASE_DIR}/GenericMOM
	APPM_DIR=${BASE_DIR}/Application-Manager
	EXE_DIR=${BASE_DIR}/Execution-Manager
	RES_DIR=${BASE_DIR}/Resource-Manager
	MON_DIR=${BASE_DIR}/Monitoring
	OffMOM_DIR=${BASE_DIR}/OfflineMOM
	USER_DIR=${BASE_DIR}/User-tools
	MBT_DIR=${BASE_DIR}/MBT
	API_FILE=${BASE_DIR}/PHANTOM_FILES
	SERVERS_DIR=/home/demo/phantom_servers

	PASS=password

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
	printf "##### Updating Monitoring API files...\n"
	printf "##################################################\n"
	cd $API_FILE &&
	which svn > /dev/null
	if [ $? -eq 1 ]; then
    		echo "Subversion is not installed"
		echo "Attempting to install..."
		echo $PASS | sudo -S echo "" &&
		sudo apt-get update && 
		sudo apt-get install -y subversion &&
		echo "subversion is installed"
	fi
	svn export --force https://github.com/PHANTOM-Platform/Monitoring/trunk/Monitoring_client Monitoring

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

	printf "\n##################################################\n"
	printf "##### Updating Parallelisation-Toolset...\n"
	printf "##################################################\n"
	cd $PT_DIR &&
	git pull

	printf "\n##################################################\n"
	printf "##### Updating Generic_MOM...\n"
	printf "##################################################\n"
	cd $MOM_DIR &&
	git pull
	
	printf "\n##################################################\n"
	printf "##### Updating Monitoring...\n"
	printf "##################################################\n"	
#	cd ${BASE_DIR}/Monitoring &&
#	svn export --force https://github.com/PHANTOM-Platform/Monitoring/trunk/Monitoring_server Monitoring_server
	cd ${MON_DIR} &&
	git pull

	printf "\n##################################################\n"
	printf "##### Updating MBT tools...\n"
	printf "##################################################\n"	
	cd ${MBT_DIR}/MBT-Test-Execution &&
	git pull

# Start servers
	cd ${THIS_DIR} &&
	bash start-servers.sh
