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
app_name = "WINGSTest3"

## Paths of folders
# Root of application (to upload makefile and cla.in)
root_path = "/home/demo/Desktop/phantom-tools/Examples/WINGStest3"

# folder with source code
src_path = "/home/demo/Desktop/phantom-tools/Examples/WINGStest3/src"

# folder with description files
desc_path = "/home/demo/Desktop/phantom-tools/Examples/WINGStest3/description"

#folder with PHANTOM API
phantom_path = "/home/demo/Desktop/phantom-tools/PHANTOM_FILES"

#Link to the where the marketplace is hosted
ipMarket_path = "https://github.com/PHANTOM-Platform/PHANTOM-IP-Core-Marketplace.git"
ip_folder = "IPCore-MarketPlace"

# folder with inputs
inputs_path = "/home/demo/Desktop/phantom-tools/HPC_UC/input"

CompNetPath = "description" 
CompNetName = "cpn.xml" #Name of the component network file to be used
#CompNetName = "Component-Network.xml_old"

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
PT_mode = "on" #operation mode: on | off - "on" to run PT normally, "off" to skip  code analysis process

## IPCore-Gen ##
# IPCore-gen Location
IP_path= "/Desktop/IP-Core-Generator/"

## DM ##
# DM location
DM_path = "/home/demo/phantom-tools/DeploymentManager"
DM_mode = "exec" #operation mode: normal | test

## MBT ##
# Performance estimation
MBT_pe_path = "/home/demo/phantom-tools/MBT/MBT-Performance-Estimation"
tested_comp_name = "TestedComponents.xml_old"
output_est_name = "EstimationResult.xml"

# Test Execution 
MBT_te_path = "/home/demo/phantom-tools/MBT/MBT-Test-Execution/Test Execution/bin"
deployment_plan = "Deployment-plan.xml"


FPGAVM_ip = "192.168.99.100"
FPGAVM_port = 2222
FPGAVM_user = "phantom"





