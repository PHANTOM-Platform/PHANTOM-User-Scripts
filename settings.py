###################################
### Repositories configurations ###
###################################

# Set the Repository IP address and port
repository_ip = "localhost"
repository_port = 8000


# Set the Application Manager websocket IP address and port
app_manager_ip = "localhost"
app_manager_port = 8500

# Set the Execution Manager IP address and port
exe_manager_ip = "localhost"
exe_manager_port = 8700

# Set the Monitoring Server IP address and port
monitoring_ip = "localhost"
monitoring_port = 3033

# Authetication credentials
user = "qwerty@ytrewq"
password = "1234"

##################################
### Application configurations ###
##################################

# Name of the application
app_name = "test_app"

## Paths of folders
# Root of application (to upload makefile and cla.in)
root_path = "/home/demo/phantom-tools/Examples/WINGStest3"

# folder with source code
src_path = "/home/demo/phantom-tools/Examples/WINGStest3/src"

# folder with description files
desc_path = "/home/demo/phantom-tools/Examples/WINGStest3/description"

# Name of the component network file to be used
comp_network= ""

# Name of platform description to be used
platf_desc = ""

# folder with inputs
inputs_path = ""

############################
### Tools Configurations ###
############################

## MOM ##
# MOM location
MOM_path = "/home/demo/phantom-tools/GenericMOM-Release20180726"
# Component network file to be used
MOM_cmp_net = "Component-Network.xml"
# Platform description to be used
MOM_plat_desc = "Platform-Description.xml"

## PT ##
# PT location
PT_path = "/home/demo/phantom-tools/ParallelizationToolset-Release20190108"
PT_mode = "test"
PT_binID = 6

## DM ##
# DM location
DM_path = "/home/demo/phantom-tools/DeploymentManager-Release20190108"
DM_mode = "normal"
DM_binID = 6

