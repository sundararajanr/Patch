#!/usr/bin/env python
import openpyxl
import yaml
import os
import time
import json
import calendar
import subprocess

from datetime import datetime
from subprocess import call

try:

     print("subprocess command started")
     
     call(["ansible-playbook", "/var/lib/awx/projects/_18__snow_project/Change_creation.yml"])
     
     #call(["ansible-playbook", "-i", "hosts", "Change_creation.yml"])
     
     print("subprocess command completed")
     
     print("Process completed")
     
     #cmd = "git --version"
     #print(os.chdir('/var/lib/awx/projects/_18__snow_project/'))
     #print(os.system('ls'))
     #print("testing ...")
     
     #returned_value = os.system(cmd)  # returns the exit code in unix
     #print('returned value:', returned_value)

except:
    print("error occured")
    raise 
