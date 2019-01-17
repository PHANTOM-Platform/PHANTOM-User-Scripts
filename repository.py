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
	repo_token_url = "http://{}:{}/signup?email={}&pw={}".format(settings.repository_ip, settings.repository_port, user, pwd)

	try:
		headers = {'content-type': 'text/plain'}
		rv = requests.post(repo_token_url, headers=headers)
		if rv.status_code != 200:
			print("Could not log in to repository. Status code: {}\n{}".format(rv.status_code, rv.text))
			return 1
		else:
			print("User: {} was successfully registred!".format(user))
		return 0
	except requests.exceptions.ConnectionError as e:
		print("ERRROR: Connection refused when connecting to the repository during registry.")
		print(str(e))
		sys.exit(1)



def uploadFile(filetoupload, token, target_path):
	repo_source = "Development"
	filename = os.path.basename(filetoupload) 

	
	if not os.path.isfile(filetoupload):
		print("{} is not a valid file.".format(filetoupload))
		sys.exit(1)
	else:
		print("Uploading {} to {}/{}/{}".format(filetoupload,settings.app_name,repo_source,target_path))


	url = "http://{}:{}/upload?project={}&source={}&DestFileName={}&Path={}".format(settings.repository_ip, settings.repository_port, settings.app_name, repo_source, filename, target_path)

	headers = {'Authorization': "OAuth {}".format(token)}

	uploadjson = "{{\"project\": \"{}\", \"source\": \"{}\", \"name\": \"{}\"}}"\
		.format(settings.app_name, repo_source, filename)

	files = {
		'UploadFile': open(filetoupload, "rb"),
		'UploadJSON': uploadjson
	}

	rv = requests.post(url, files=files, headers=headers)

	if rv.status_code != 200  and rv.status_code != 420:
		print("Could not upload file to repository. Status code: {}\n{}".format(rv.status_code, rv.text))
		sys.exit(1)

	
	websocketUpdate(headers, settings.app_name, repo_source)
	

	
			
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
