#!/usr/bin/env python3

from os import listdir, walk
from os.path import isfile, join, exists, dirname

import argparse, sys, subprocess, socket
import settings, repository

token_file = "token.txt"

parser = argparse.ArgumentParser(description='Tool to support the execution of an application on PHANTOM Framework')
parser.add_argument('-u', '--noUpload', dest='noUpload', action='store_true' , help='Do not (re)upload the application to the repository. (Application should be already in repository)')
parser.add_argument('-d', '--onlyDesc', dest='descriptionOnly', action='store_true' , help='Only re-uploads the description files to the repository)')
parser.add_argument('-i', '--skipInputs', dest='noInputs', action='store_true' , help='Do not (re)upload the application inputs to the repository. (Inputs should be already in repository)')
parser.add_argument('-c', '--clean', dest='clean', action='store_true' , help='Clean all the data in repositories and temporary cache on PHANTOM tools. Automatically update PHANTOM_FILES (-p)')
parser.add_argument('-m', '--ipmarket', dest='ipMarket', action='store_true' , help='Uploads the IP Core Market place to the repository')
parser.add_argument('-p', '--phantomfiles', dest='phFiles', action='store_true' , help='Uploads the PHANTOM files (PHANTOM API and Monitoring API)')
parser.add_argument('--Tpe', dest='MBTpe', action='store_true' , help='Runs only the MBT Performannce estimation tool')
parser.add_argument('--Tte', dest='MBTte', action='store_true' , help='Runs only the MBT Test Execution tool')

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def externalizeIP(ip):
	if ip == "localhost":
		return getIP()
	else:
		return ip

config_decoder = {
	"user": ["#USER#", settings.user],
	"pwd" : ["#PWD#", settings.password],
	"repo_ip" : ["#REPO_IP#", externalizeIP(settings.repository_ip)],
	"repo_port" : ["#REPO_PORT#", settings.repository_port],
	"appman_ip" : ["#APPMAN_IP#",settings.app_manager_ip],
	"appman_port" : ["#APPMAN_PORT#", settings.app_manager_port],
	"exeman_ip" : ["#EXE_IP#", settings.exe_manager_ip],
	"exeman_port" : ["#EXE_PORT#", settings.exe_manager_port],
	"mon_ip" : ["#MON_IP#", settings.monitoring_ip],
	"mon_port" : ["#MON_PORT#", settings.monitoring_port],
	"res_ip" : ["#RES_IP#", settings.resource_ip],
	"res_port" : ["#RES_PORT#", settings.resource_port],
	"app_name" : ["#APPNAME#", settings.app_name],
	"token" : ["#TOKEN#", "No_Token"],
	"PT_mode" : ["#PT_MODE#",settings.PT_mode],
	"CompPath" : ["#COMPNETPATH#",settings.CompNetPath],
	"CompName" : ["#COMPNETNAME#",settings.CompNetName],
	"PlatPath" : ["#PLATDESPATH#",settings.PlatDesPath],
	"Platname" : ["#PLATDESNAME#",settings.PlatDesName],
	"DM_mode" : ["#DM_MODE#",settings.DM_mode],
	"dep_plan" : ["#DEP_PLAN#", settings.deployment_plan],
	"mbt_test_comp" : ["#TEST_COMP#",settings.tested_comp_name],
	"mbt_output_test" : ["#OUTOUT_TEST#", settings.output_est_name]
}



def main():
	
	args = parser.parse_args()

	if args.clean:
		process=subprocess.Popen(['bash','/home/demo/Desktop/phantom-tools/User-tools/management-scripts/clean-installation.sh'],
		         stdin=subprocess.PIPE,
		         stdout=subprocess.PIPE,
		         stderr=subprocess.PIPE,cwd="./management-scripts")
		stdoutdata,stderrdata=process.communicate(input=b'y\n')
		process.wait()
		print(stdoutdata)
		print(stderrdata)

	#authentication verification
	auth_token = getToken()
	
	config_decoder["token"]=["#TOKEN#", auth_token]

	if args.MBTpe: #runs only MBT Performance estimation
		generateConfigFile('MBTpe',settings.MBT_pe_path, "PerformanceEstimator.py", ["mbt_test_comp","mbt_output_test"])

		newTerminal(settings.MBT_pe_path,'python3 PerformanceEstimator.py ' + settings.CompNetName, 'MBT Perf Est')


	elif args.MBTte: #runs only mBT Test Execution
		generateConfigFile('MBTte',settings.MBT_te_path, "MyExample.cfg", ["user", "pwd", "repo_ip", "repo_port", "appman_port", "exeman_port", "res_port", "mon_port", "app_name", "dep_plan", "token"])

		newTerminal(settings.MBT_te_path,'ttcn3_start ./mbttest MyExample.cfg', 'MBT Test Exec')


	else: #runs other options


		if args.ipMarket:
			#Downloads Ipcores
			print("Downloading Marketplace...")
			code = subprocess.call(['git','clone',settings.ipMarket_path,settings.ip_folder])
		
			if code == 0:
				print("Uploading IP Cores...")
				uploadMarket(settings.ip_folder, auth_token,"")
				print("Cleaning local marketplace")
				code = subprocess.call(['rm','-rf',settings.ip_folder])
			else:
				print("Unable to download the IPCore Marketplace")
	

		if not args.noUpload:
			#upload source code
			if settings.root_path != '' and (not args.descriptionOnly):
				uploadRootFiles(settings.root_path, auth_token)
				print("Uploading")

			if settings.src_path != '' and (not args.descriptionOnly):
				print("Uploading source code...")
				uploadAllFiles(settings.src_path, auth_token, "src")

			#upload descriptions

			if settings.desc_path != '':
				print("Uploading description files...")
				uploadAllFiles(settings.desc_path, auth_token, "description")

		#upload PHANTOM_FILES
	
		if (args.phFiles or args.clean) and settings.phantom_path != '':
			print("Uploading PHANTOM files")

			uploadPHANTOM_FILES(settings.phantom_path, auth_token,"")
		

		if not args.noInputs:
			#upload inputs
			if settings.inputs_path != '':
				print("Uploading description files...")
				uploadAllFiles(settings.inputs_path, auth_token, "inputs")	

	


		#register app in application manager
		repository.websocketUpdateStatus(settings.app_name, "development", "finished", auth_token)

		#configure and start MOM
		generateConfigFile('MOM',settings.MOM_path, "configuration.xml", ["user", "pwd", "repo_ip", "repo_port", "appman_port", "exeman_port", "app_name", "CompName", "Platname"])

		newTerminal(settings.MOM_path,'/usr/bin/java -jar GA_MOM.jar --manualData --online', 'MOM')

		#configure and start PT

		generateConfigFile('PT',settings.PT_path, "config.properties", ["user", "token", "repo_ip", "repo_port", "appman_ip","appman_port", "mon_ip","mon_port", "app_name", "PT_mode", "CompPath", "CompName", "PlatPath", "Platname", "exeman_ip", "exeman_port"])

		newTerminal(settings.PT_path,'/usr/bin/java -jar ParallelizationToolset.jar', 'PT')
	

		#configure and start IPCore-GEN

	#	generateConfigFile("IPGEN",settings.IP_path, "settings.py", ["user", "pwd", "repo_ip", "repo_port", "appman_ip","appman_port", "CompName"])

	#	newTerminal(settings.IP_path,'/usr/bin/python3 ipcore-generator.py subscribe ' + settings.app_name, 'IPCore-Gen')
	
		#configure and start DM

		generateConfigFile('DM',settings.DM_path, "config.properties", ["user", "token", "repo_ip", "repo_port", "appman_ip","appman_port", "mon_ip","mon_port", "app_name", "DM_mode","exeman_ip", "exeman_port", "CompPath", "CompName", "PlatPath", "Platname",  "exeman_ip", "exeman_port","res_ip","res_port"])
		newTerminal(settings.DM_path,'/usr/bin/java -jar DeploymentManager.jar','DM')
	
def getToken():
	try: #attempts to read token
		f=open(token_file,"r")
		print("Token file found")
		token=f.read()
		if repository.isTokenValid(token) is True:
			return token
		else:
			print("Token is invalid!!!")
			token = getNewToken()

	except: #token not found
		print("Token file not found. Attempting login")
		token = getNewToken()

		if token == -1:
			sys.exit(1)
		else:
			print("Authentication successfull. Saving token...")
	f = open(token_file,"w")
	f.write(str(token))
	f.close()
	print("Token saved!")
	return token	


def getNewToken():
	token=repository.authenticate(settings.user,settings.password)

	if token == 1:
		print("Attempting to create a new user") # should we really do this?
		if repository.register(settings.user,settings.password) == 0:
			print("User registered with success. Starting authentication")
			token=repository.authenticate(settings.user,settings.password)

			if token == 1:
				return -1

		else:
			print("Error during registering!!!!")
			return -1
	
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

def uploadRootFiles(pathdir, token):
	rootFiles = {"Makefile","cla.in"}
	fnames = listdir(pathdir)
	for f in fnames:
		filepath=join(pathdir, f)
		if isfile(filepath) and f in rootFiles:
			repository.uploadFile(filepath, token, relativePath(pathdir, "", filepath), settings.app_name,"development")


def uploadAllFiles(path_dir, token, repo_folder):
	files = listFiles(path_dir)

	for filePath in files:
		repository.uploadFile(filePath, token, relativePath(path_dir, repo_folder, filePath), settings.app_name,"development")


def uploadPHANTOM_FILES(path_dir, token, repo_folder):
	files = listFiles(path_dir)

	for filePath in files:
		source = "DM" if ("/DM/" in filePath) else "Monitoring"
#		repository.uploadFile(filePath, token, relativePath(path_dir, repo_folder, filePath), "PHANTOM_FILES","DM" if ("/DM/" in filePath) else "Monitoring")
		repository.uploadFile(filePath, token, relativePath(path_dir + '/' + source + '/', repo_folder, filePath), "PHANTOM_FILES",source)


def uploadMarket(path_dir, token, repo_folder):
	files = listFiles(path_dir)

	for filePath in files:
		repository.uploadFile(filePath, token, relativePath(path_dir, repo_folder, filePath), "IPCore-Marketplace","DM")

def relativePath(root, repo_folder,fullPath):
	path =  fullPath.replace(root,'')
	remote_path =  str(repo_folder) + dirname(path)
	if remote_path != '' and remote_path[-1] == '/':
		return remote_path[:-1]
	else:
		return remote_path



def generateConfigFile(toolID,dir_path,configFileName,listToConfigure):
	dir_path = enforce_trailing_slash(dir_path)
	print("templates/" + toolID + "-configuration-template.txt")
	try:
		f_template = open("templates/" + toolID + "-configuration-template.txt", "r")
		template = f_template.read()
	
	except:
		print("Template file not found")
		sys.exit(1)

	for config in listToConfigure:
		[pattern, value] = config_decoder[config]
		template = template.replace(pattern,str(value))
		
	f_template = open(dir_path + configFileName, "w")
	f_template.write(template)
	f_template.close()
	print("")


def generateRemoteConfigFile(dir_path,configFileName,listToConfigure):
	dir_path = enforce_trailing_slash(dir_path)
	try:
		f_template = open(dir_path + "/configuration-template.txt", "r")
		template = f_template.read()
	
	except:
		print("Template file not found")
		sys.exit(1)

	for config in listToConfigure:
		[pattern, value] = config_decoder[config]
		if value == "localhost":
			value = getIP()
		template = template.replace(pattern,str(value))
		
	f_template = open(dir_path + configFileName, "w")
	f_template.write(template)
	f_template.close()
	print("")
		

def newTerminal(workdir,command,title):
#	return subprocess.Popen(['gnome-terminal' ,'--profile=NoClosing', '--working-directory=' + workdir, '-x'] + command)	
	return subprocess.Popen(['xterm' ,'-s','-si','-sk','-sb','-hold','-fa', 'Monospace', '-fs','11','-T',title, '-e' ,command],cwd=workdir)	

# Utils

def enforce_trailing_slash(path):
	'''
	Returns path, with the '/' character appended if it did not already end with it
	'''
	if path[-1] != '/':
		return path + '/'
	else:
		return path

def externalizeIP(ip):
	if ip == "localhost":
		return getIP()
	else:
		return ip
	

def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


if __name__ == "__main__":
	main()



		
		




