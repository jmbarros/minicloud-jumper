# How use jumper
## Creating servers
- create at least 4 servers, for example:
  - jumper01
  - master01
  - worker01
  - proxy01
  
 - into jumper01:
  - execute: curl -l https://raw.githubusercontent.com/jmbarros/minicloud-jumper/master/jumper.py | python
  - edit: inventory file with the hostnames and passwords 
  - execute: python servers/install.py
  

  that's it!
