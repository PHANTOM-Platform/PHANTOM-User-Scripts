import requests, os, sys
import settings

def authenticate(user,pwd):
	"""
	Authenticates with the repository
	Returns the OAuth token, or exits if authentication fails.
	"""
	repo_token_url = "http://{}:{}/login?email={}&pw={}".format(settings.repository_ip, settings.repository_port, user, pwd)

	try:
		headers = {'content-type': 'text/plain'}
		rv = requests.get(repo_token_url, headers=headers)
		if rv.status_code == 200:
			print("Authentication sucessfull")
			return rv.text
		elif rv.status_code == 401:
			print("Credentials invalid!!!")
			return 1
		else:
			print("Could not log in to repository. Status code: {}\n{}".format(rv.status_code, rv.text))
			ys.exit(1)
	except requests.exceptions.ConnectionError as e:
		print(ANSI_RED + "Connection refused when connecting to the repository. " + ANSI_END)
		print(str(e))
		sys.exit(1)

def register(user,pwd):
	"""
	Register a new user in the repository
	"""

	servers = {
		"Repository": (settings.repository_ip, settings.repository_port),
		"Application Manager": (settings.app_manager_ip, settings.app_manager_port), 
		"Execution Manager": (settings.exe_manager_ip, settings.exe_manager_port), 
		"Monitoring Server": (settings.monitoring_ip, settings.monitoring_port)
		}

	failures = 0
	for name, address in servers.items():

		repo_token_url = "http://{}:{}/signup?email={}&pw={}".format(address[0], address[1], user, pwd)
		try:
			headers = {'content-type': 'text/plain'}
			rv = requests.post(repo_token_url, headers=headers)
			serverFlush(address[0], address[1])
			if rv.status_code != 400:
				print("Could not log in to {} repository. Status code: {}\n{}".format(name, rv.status_code, rv.text))
				failures +=1
			else:
				print("User: {} was successfully registred in {}!".format(user, name))
				
		except requests.exceptions.ConnectionError as e:
			print("ERRROR: Connection refused when connecting to the {} repository during registry.".format(name))
			print(str(e))
			failures += 1

	
	total_servers = len(servers)	
	print(" User {} registered in {} of {} servers".format(user, total_servers-failures, total_servers))
	if failures < total_servers:
		return 0
	else:
		return 1


def isTokenValid(token):
	url = "http://{}:{}/verifytoken".format(settings.repository_ip, settings.repository_port)
	headers = {'Authorization': "OAuth {}".format(token)}
	rv = requests.get(url, headers=headers)
	if rv.status_code == 200:
		return True
	else:
		return False
	
	

def uploadFile(filetoupload, token, target_path, repo_project, repo_source):
	
	filename = os.path.basename(filetoupload) 

	
	if not os.path.isfile(filetoupload):
		print("{} is not a valid file.".format(filetoupload))
		sys.exit(1)
	else:
		print("Uploading {} to {}/{}/{}".format(filetoupload,repo_project,repo_source,target_path))


	url = "http://{}:{}/upload?project={}&source={}&DestFileName={}&Path={}".format(settings.repository_ip, settings.repository_port, repo_project, repo_source, filename, target_path)

	headers = {'Authorization': "OAuth {}".format(token)}

	uploadjson = "{{\"project\": \"{}\", \"source\": \"{}\", \"name\": \"{}\"}}"\
		.format(repo_project, repo_source, filename)

	files = {
		'UploadFile': open(filetoupload, "rb"),
		'UploadJSON': uploadjson
	}

	rv = requests.post(url, files=files, headers=headers)

	if rv.status_code != 200  and rv.status_code != 420:
		print("Could not upload file to repository. Status code: {}\n{}".format(rv.status_code, rv.text))
		sys.exit(1)

	
			
def websocketUpdate(headers, project, repo_source):
	"""
	Ping an update to the Application Manager for the project
	"""
	uploadjson = "{{\"project\": \"{}\", \"source\": \"{}\"}}".format(project, repo_source)

	url = "http://{}:{}/update_project_tasks".format(settings.app_manager_ip, settings.app_manager_port)

	rv = requests.post(url, files={'UploadJSON': uploadjson}, headers=headers)

	if rv.status_code != 200 and rv.status_code != 420:
		print("Could not update task. Status code: {}\n{}".format(rv.status_code, rv.text))
		sys.exit(1)

def websocketUpdateStatus(project, source, status,token):
	"""
	Ping an update to the Application Manager for the project
	"""

	
	headers = {'Authorization': "OAuth {}".format(token)}
	
	uploadjson = "{{\"project\": \"{}\", \"{}\":{{\"status\":\"{}\"}} }}".format(project, source, status)
	
	url = "http://{}:{}/update_project_tasks".format(settings.app_manager_ip, settings.app_manager_port)

	rv = requests.post(url, files={'UploadJSON': uploadjson}, headers=headers)

	if rv.status_code != 200 and rv.status_code != 420:
		print("Could not update task. Status code: {}\n{}".format(rv.status_code, rv.text))
		sys.exit(1)
	
	serverFlush(settings.app_manager_ip, settings.app_manager_port)



def serverFlush(serverIP,ServerPort):
	url = "http://{}:{}/_flush".format(serverIP,ServerPort)
	requests.get(url)

