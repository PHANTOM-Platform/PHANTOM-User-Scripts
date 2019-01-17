#!/usr/bin/env python3

from os import listdir, walk
from os.path import isfile, join, exists, dirname

import argparse, sys, subprocess
import settings, repository

token_file = "token.txt"

config_decoder = {
	"user": ["#USER#", settings.user],
	"pwd" : ["#PWD#", settings.password],
	"repo_ip" : ["#REPO_IP#", settings.repository_ip],
	"repo_port" : ["#REPO_PORT#", settings.repository_port],
	"appman_ip" : ["#APPMAN_IP#",settings.app_manager_ip],
	"appman_port" : ["#APPMAN_PORT#", settings.app_manager_port],
	"exeman_ip" : ["#EXE_IP#", settings.exe_manager_ip],
	"exeman_port" : ["#EXE_PORT#", settings.exe_manager_port],
	"mon_ip" : ["#MON_IP#", settings.monitoring_ip],
	"mon_port" : ["#MON_PORT#", settings.monitoring_port],
	"app_name" : ["#APPNAME#", settings.app_name],
	"token" : ["#TOKEN#", "No_Token"],
	"PT_mode" : ["#PT_MODE#",settings.PT_mode],
	"PT_binID" : ["#PT_BIN_ID#",settings.PT_binID],
	"DM_mode" : ["#DM_MODE#",settings.DM_mode],
	"DM_binID" : ["#DM_BIN_ID#",settings.DM_binID]
	
}

def main():
	
	#authentication verification
	auth_token = getToken()
	
	config_decoder["token"]=["#TOKEN#", auth_token]

	#upload source code

	if settings.src_path != '':
		print("Uploading source code...")
		uploadAllFiles(settings.src_path, auth_token, "src")

	#upload descriptions

	if settings.desc_path != '':
		print("Uploading description files...")
		uploadAllFiles(settings.desc_path, auth_token, "description")

	#upload inputs
	if settings.inputs_path != '':
		print("Uploading description files...")
		uploadAllFiles(settings.inputs_path, auth_token, "inputs")	

	#register app in application manager

	#configure and start MOM
	generatetConfigFile(settings.MOM_path, "configuration.xml", ["user", "pwd", "repo_ip", "repo_port", "appman_port", "exeman_port", "app_name"])

	newTerminal(settings.MOM_path,['/usr/bin/java', '-jar', 'GA_MOM.jar','--online'])

	#configure and start PT

	generatetConfigFile(settings.PT_path, "config.properties", ["user", "token", "repo_ip", "repo_port", "appman_ip","appman_port", "mon_ip","mon_port", "app_name", "PT_mode", "PT_binID"])

	newTerminal(settings.PT_path,['/usr/bin/java', '-jar', 'ParallelizationToolset-Release20190108.jar'])
	
	#configure and start DM

	generatetConfigFile(settings.DM_path, "config.properties", ["user", "token", "repo_ip", "repo_port", "appman_ip","appman_port", "mon_ip","mon_port", "app_name", "DM_mode", "DM_binID"])
	newTerminal(settings.DM_path,['/usr/bin/java', '-jar', 'DeploymentManager-Release20190108.jar'])
	
def getToken():
	try: #attempts to read token
		f=open(token_file,"r")
		print("Token file found")
		return f.read()

	except: #token not found
		print("Token file not found. Attempting login")
		token=repository.authenticate(settings.user,settings.password)

		if token == 1:
			print("Attempting to create a new user") # should we really do this?

			if repository.register(settings.user,settings.password) == 0:
				print("User registered with success. Starting authentication")
				token=repository.authenticate(settings.user,settings.password)

				if token == 1:
					sys.exit(1)

		print("Authentication successfull. Saving token...")
		f = open(token_file,"w")
		f.write(token)
		f.close()
		print("Token saved!")
		return token

					
		

def listFiles(path_dir):
	"""
	Identifies all the files under a specific directory. Navegates across sub-directories.
	Returns a dictionary with key: dir path; value: list of files in dir
	"""
	allfiles = []
	for root, dirs, files in walk(path_dir):
		for name in files:
			allfiles.append(join(root,name))
	return allfiles


def uploadAllFiles(path_dir, token, repo_folder):
	files = listFiles(path_dir)
	
	for filePath in files:
		repository.uploadFile(filePath, token, relativePath(path_dir, repo_folder, filePath))



def relativePath(root, repo_folder,fullPath):
	path =  fullPath.replace(root,'')
	remote_path =  str(repo_folder) + dirname(path)
	if remote_path[-1] == '/':
		return remote_path[:-1]
	else:
		return remote_path



def generatetConfigFile(dir_path,configFileName,listToConfigure):
	dir_path = enforce_trailing_slash(dir_path)
	try:
		f_template = open(dir_path + "/configuration-template.txt", "r")
		template = f_template.read()
		print("Configuration Template Loaded")
	
	except:
		print("Template file not found")
		sys.exit(1)

	for config in listToConfigure:
		[pattern, value] = config_decoder[config]
		template = template.replace(pattern,str(value))
		
	f_template = open(dir_path + configFileName, "w")
	f_template.write(template)
	f_template.close()
		

def newTerminal(workdir,command):
	return subprocess.Popen(['gnome-terminal' ,'--profile=NoClosing', '--working-directory=' + workdir, '-x'] + command)	

# Utils

def enforce_trailing_slash(path):
	'''
	Returns path, with the '/' character appended if it did not already end with it
	'''
	if path[-1] != '/':
		return path + '/'
	else:
		return path



if __name__ == "__main__":
	main()



		
		




