#!/usr/bin/python 
#create inception
### todo
# add check slcli file
#######################################################################
#defs

import os

def yum_install ( pkg ):
   "install via yum"
   install = "yum install -y  " + pkg
   os.system(install)
   return;

def cmd ( cmdx ):
   " run"
   os.system(cmdx)
   return;

def copy ( ori, dest ):
   " coping file "
   cpw = "cp -r " + ori + " " + dest
   os.system(cpw)
   return;
 ############
yum_install("wget")
cmd("wget http://172.24.10.78/icp/ibm-cloud-private-x86_64-2.1.0.tar.gz ~/.")
cmd("tar -xf ibm-cloud-private-x86_64-2.1.0.tar.gz -O | docker load")
