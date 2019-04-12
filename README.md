# PHANTOM-User-Scripts

Tools designed to aid a User to configure and interact with PHANTOM tools. The purpose of these tools is to automatize most of the work needed, handling the authentication and registering processes, configuration, and execution of PHANTOM tools.

Before running any tool, <b> the User must update the configurations first </b>. These configurations are stored in the file `settings.py`.
In this file, the user should validate and update several fields. This file is composed of three main sections:

1. **Repositories configurations** – used for the USER specify the location of the repositories to be used (localhost or remote location) and credentials. E.g.:
```python
   # Set the Repository IP address and port 
   #repository_ip = "141.58.0.8" 
   #repository_port = 2777
    repository_ip = "localhost"
    repository_port = 8000
    
    # Authentication credentials
    user =
    password =
 ```
 
2. **Application configurations** – Used for the USER to indentify application specific properties:
Name of the application to be used server and by PHANTOM tools to identify the application:

```python
  app_name = "WINGStest3"
 ```

Path for the root of the application‟s folder (to upload makefile and cla.in)

```python
  root_path = "/home/demo/phantom-tools/Examples/WINGStest3"
```

Path for the folder with the source code

```python
  src_path = "/home/demo/phantom-tools/Examples/WINGStest3/src"
```

Path for the folder with description files (Component Network and Platform Description)

```python
  desc_path = "/home/demo/phantom- tools/Examples/WINGStest3/description"
```
Path for thevfolder with PHANTOM API files

```python
  phantom_path = "/home/demo/Desktop/phantom- tools/PHANTOM_FILES"
```

Link to the where the marketplace is hosted and name of the folder where IPCores shoul be stored locally

```python
  ipMarket_path = "https://github.com/PHANTOM-Platform/PHANTOM- IP-Core-Marketplace.git"
  ip_folder = "IPCore-MarketPlace"
```

Path for folder with application inputs

```python
  inputs_path = ""
```

Name of the component network file to be used

```python
  CompNetName = "cpn.xml"
```

Name of the platform description file to be used

```python
  PlatDesName = "hw_local.xml"
```

3. **Tools Configurations** – This section contains the parameters for configuring the PHANTOM tools. In includes the path for each tool deployed on the machine. E.g.:

```python
  # MOM location
  MOM_path = "/home/demo/phantom-tools/GenericMOM"
```

And tool specific arguments. E.g.:

```python
  PT_mode = "on" #operation mode: on | off - "on" to run PT normally, "off" to skip code analysis process
```
  In this section can also be found the property for the address of the FPGA VM, as well as the SSH port to be used
  
```python
  FPGAVM_ip = “”
  FPGAVM_port =
```

<b> After the configuration of the `settings.py`, the user needs to open a terminal and run the command:</b>

`./start-PHANTOM.py`

usage: start-PHANTOM.py [-h] [-u] [-i] [-c] [-m] [-p]

Tool to support the execution of an application on PHANTOM Framework

optional arguments:

  -h, --help          show this help message and exit

  -u, --noUpload      Do not (re)upload the application to the repository.
                      (Application should be already in repository)

  -i, --skipInputs    Do not (re)upload the application inputs to the
                      repository. (Inputs should be already in repository)

  -c, --clean         Clean all the data in repositories and temporary cache
                      on PHANTOM tools

  -m, --ipmarket      Uploads the IP Core Market place to the repository

  -p, --phantomfiles  Uploads the PHANTOM files (PHANTOM API and Monitoring
                      API)
  
  --Tpe               Runs only the MBT Performance estimation tool
  
  --Tte               Runs only the MBT Test Execution tool


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
