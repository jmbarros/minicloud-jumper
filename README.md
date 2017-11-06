# How to use jumper
## Creating server

- create 1 virtual server, running Centos 7 
	- download here: http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1708.iso)
	- recommended virtual hardware: 2 vCPUs + 8 GB RAM + 100 GB vDISK 

- download the ICP-EE at IBM XL
	- link: http://w3-103.ibm.com/software/xl/download/ticket.do 

- login virtual server
  - execute: curl -l https://raw.githubusercontent.com/jmbarros/minicloud-jumper/master/jumper.py | python

  - edit: "inventory" file with the hostname and password

  - execute: python servers/icp-ee.py

  - execute: python servers/install.py
  
  that's it!
