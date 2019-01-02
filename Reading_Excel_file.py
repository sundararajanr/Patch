#!/usr/bin/env python
import openpyxl
import yaml
import os
import time
import json
import calendar
from datetime import datetime

try:

     cmd = "git --version"

     #returned_value = os.system(cmd)  # returns the exit code in unix
     #print('returned value:', returned_value)
     os.system ('ansible-playbook ./Change_creation.yml')

except:
    print("error occured")
    raise 

