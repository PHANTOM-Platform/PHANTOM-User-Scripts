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
user = "marcio.mateus@unparallel.pt"
password = "9834376081"

##################################
### Application configurations ###
##################################

# Name of the application
app_name = "WINGStest33"

## Paths of folders
# Root of application (to upload makefile and cla.in)
root_path = "/home/demo/phantom-tools/Examples/WINGStest3"

# folder with source code
src_path = "/home/demo/phantom-tools/Examples/WINGStest3/src"

# folder with description files
desc_path = "/home/demo/phantom-tools/Examples/WINGStest3/description"

#folder with PHANTOM API
phantom_path = "/home/demo/Desktop/phantom-tools/PHANTOM_FILES/DM"

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
MOM_cmp_net = "Component-Network.xml"
# Platform description to be used
MOM_plat_desc = "Platform-Description.xml"

## PT ##
# PT location
PT_path = "/home/demo/phantom-tools/ParallelizationToolset"
#PT_mode = "normal" #operation mode: normal | test
PT_mode = "exec"
PT_binID = 6 #



## DM ##
# DM location
DM_path = "/home/demo/phantom-tools/DeploymentManager"
DM_mode = "exec" #operation mode: normal | test
DM_binID = 6

