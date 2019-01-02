#!/usr/bin/env python
import openpyxl
import yaml
import os
import time
import json
import calendar
from datetime import datetime

try:

     os.system('/bin/ansible-playbook /var/lib/awx/projects/_18__snow_project/Change_creation.yml') 
     cmd = "git --version"
     print(os.chdir('/var/lib/awx/projects/_18__snow_project/'))
     print(os.system('ls'))
     print("testing ...")
     
     #returned_value = os.system(cmd)  # returns the exit code in unix
     #print('returned value:', returned_value)

except:
    print("error occured")
    raise 
