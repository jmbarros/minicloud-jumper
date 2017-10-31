# How use jumper
## Creating servers
- create 1 servers, for example:

	- minicloud01
  
 - into minicloud01:
  - execute: curl -l https://raw.githubusercontent.com/jmbarros/minicloud-jumper/master/jumper.py | python

  - edit: "inventory" file with the hostname and password

  - execute: python servers/icp-ee.py

  - execute: python servers/install.py
  
  that's it!
