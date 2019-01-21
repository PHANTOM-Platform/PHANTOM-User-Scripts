# PHANTOM-User-Scripts

Tools designed to aid a User to configure and interact with PHANTOM tools. The purpose of these tools is to automatize most of the work needed, handling the authentication and registering processes, configuration, and execution of PHANTOM tools.

Before running any tool, the User must update the configurations first. These configurations are stored in the file `settings.py`.
In this file, the user should validate and update several fields. This file is composed of three main sections:
- First is a section where the user should update the port and address of the repositories, as well as define the credentials for authentication in the servers
- The second section corresponds to an area where the user provides some information about the application to be analysed bu PHANTOM tools, where is identified the name of the app and the path where the files are stored
- In the last  section, can be defined some tool-specific configurations like the path to where each tool is deployed and some arguments required to the correct execution each tool 

After the configuration of the `settings.py`, the user needs to open a terminal and run the command:

`./upload-app.py`

This command will:
1. Try to authenticate the user on the Repository and get the corresponding authentication token
- If the authentication fails, it attempts to register the user on all servers
2. Uploads the user application to the repository following the convention:
```
“Project”:App_Name #name of the application
  “Source”:”development”
    path:src # source code
    path:description # component network, platform description...
    path:inputs # inputs to be used by the application
```
3. Generates the configuration file for each tool (PT, MOM, and DM) based on the information on `settings.py` and on the template file `configuration-template.txt` of each tool
4. Starts the configured tools
