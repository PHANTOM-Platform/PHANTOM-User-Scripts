#!/bin/bash

# GLOBAL Variables
	BASE_DIR=$(pwd)/../../
	REPO_DIR=${BASE_DIR}/Repository
	EXE_DIR=${BASE_DIR}/Execution-Manager
	APP_DIR=${BASE_DIR}/Application-Manager
	PT_DIR=${BASE_DIR}/ParallelizationToolset
	DM_DIR=${BASE_DIR}/DeploymentManager
	MOM_DIR=${BASE_DIR}/GenericMOM
	SCRIPT_DIR=$(pwd)/../
	
echo "#########################################"
echo "########### Cleaning Servers ############"
echo "#########################################"
echo 
echo "########## Cleaning Repository ##########"
# Change wordir to scripts folder
	cd ${REPO_DIR}/api_bash_scripts &&


# Delete current DB
	bash delete_db.sh &&

# Create new DB
	bash create_db.sh

echo "########## Cleaning Execution Manager ##########"
# Clear Execution Manager
	# Delete Manaber DB
	curl -XDELETE localhost:9400/exec_manager_db

	#Setup new Execution Manager
	cd ${EXE_DIR} &&
	bash setup-new-execmanager-server.sh



echo "########## Cleaning Application Manager ##########"	
# Clear Application Manager
	# Delete Application Manager
	curl -XDELETE localhost:9400/app_manager_db

	#Setup new Application Manager
	cd ${APP_DIR} &&
	bash setup-new-app-manager-server.sh

echo "####### Removing Authentication Token #######"
	cd ${SCRIPT_DIR} &&
	rm -f token.txt

echo


echo "#########################################"
echo "############ Cleaning Tools #############"
echo "#########################################"
echo
	shopt -s extglob 
echo "############ Cleaning MOM #############"

	cd ${MOM_DIR} &&
	rm -rf -- !(GA_MOM.jar)

echo
echo "############ Cleaning PT #############"
	
	cd ${PT_DIR} &&
	rm -rf -- !(ParallelizationToolset.jar)

echo
echo "############ Cleaning DM #############"
	
	cd ${DM_DIR} &&
	rm -rf -- !(DeploymentManager.jar)






