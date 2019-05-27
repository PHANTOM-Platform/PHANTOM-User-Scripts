###################################
### Repositories configurations ###
###################################

# Set the Repository IP address and port
#repository_ip = "141.58.0.8"
#repository_port = 2777
repository_ip = "localhost"
repository_port = 8000


# Set the Application Manager websocket IP address and port
#app_manager_ip = "141.58.0.8"
#app_manager_port = 2778
app_manager_ip = "localhost"
app_manager_port = 8500

# Set the Execution Manager IP address and port
#exe_manager_ip = "141.58.0.8"
#exe_manager_port = 2781
exe_manager_ip = "localhost"
exe_manager_port = 8700

# Set the Monitoring Server IP address and port
#monitoring_ip = "141.58.0.8"
#monitoring_port = 2729
monitoring_ip = "localhost"
monitoring_port = 3033

# Set the Resource Manager IP address and port
#resource_ip = "141.58.0.8"
#resource_port = 2780
resource_ip = "localhost"
resource_port = 8600


# Authetication credentials
user = "user_lite"
password = "1234asdf"


##################################
### Application configurations ###
##################################

# Name of the application
app_name = "tutorial"

## Paths of folders
# Root of application (to upload makefile and cla.in)
root_path = "/home/demo/examples/tutorial"

# folder with source code
src_path = "/home/demo/examples/tutorial/src"

# folder with description filescd 
desc_path = "/home/demo/examples/tutorial/description"

#folder with PHANTOM API
phantom_path = "/home/demo/Desktop/phantom-tools/PHANTOM_FILES"

# folder with inputs
inputs_path = ""

CompNetPath = "description" 
CompNetName = "cpn.xml" #Name of the component network file to be used
PlatDesPath = "description"
PlatDesName = "hw_local.xml"   #Name of the platform description file to be used

############################
### Tools Configurations ###
############################

## MOM ##
# MOM location
MOM_path = "/home/demo/phantom-tools/GenericMOM"
# Component network file to be used
MOM_cmp_net = "cpn.xml"
# Platform description to be used
MOM_plat_desc = "hw_local.xml"

## PT ##
# PT location
PT_path = "/home/demo/phantom-tools/Parallelisation-Toolset"
#PT_mode = "normal" #operation mode: normal | test
PT_mode = "on"



## DM ##
# DM location
DM_path = "/home/demo/phantom-tools/Deployment-Manager"
DM_mode = "exec" #operation mode: normal | test

