# How use jumper
## Creating servers
- create at least 4 servers, for example:
  - jumper01
  - master01
  - worker01
  - proxy01
  
 - into jumper01:
  - execute: curl -l https://raw.githubusercontent.com/jmbarros/jumper/master/jumper.py | python
  - execute: ansible-playbook jumper/jumper.yml
  - edit: inventory file with the hostnames and passwords 
  - execute: python servers/config_prereq.py
  

  that's it!
