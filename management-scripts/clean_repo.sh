#!/bin/bash

# GLOBAL Variables
	BASE_DIR=$(pwd)/../../
	REPO_DIR=${BASE_DIR}/Repository

# Change wordir to scripts folder
	cd ${REPO_DIR}/api_bash_scripts


# Delete current DB
	bash delete_db.sh

# Create new DB
	bash create_db.sh


