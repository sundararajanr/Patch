#!/usr/bin/env python
import openpyxl
import yaml
import os
import time
import json
import calendar
from datetime import datetime
wb =openpyxl.load_workbook('/var/lib/awx/projects/_15__test_project/Server_Inventory_Linux.xlsx')
source = wb['Sheet1']
user_data = wb.get_sheet_by_name('Sheet1')
print(user_data.max_row)

def create_change(date,desc):
    stream=open('/var/lib/awx/projects/_15__test_project/Change_creation.yml','r')    
    data = yaml.load(stream)
    #data=yaml.load(stream)
#    print(data)
    data[0]['tasks'][0]['snow_record']['data']['short_description']=desc
    data[0]['tasks'][0]['snow_record']['data']['start_date']=date
    #print(data[0]['tasks'][0]['snow_record']['data']['short_description'])
    #print(data[0]['tasks'][0]['snow_record']['data']['start_date'])
    stream = open('/var/lib/awx/projects/_15__test_project/Change_creation.yml', 'w')
    yaml.dump(data,stream, default_flow_style=False)
#    #print(yaml.dump(data))


for x in range(1,user_data.max_row+1):
    #print(str(user_data[x][3].value))  # ------ Release date---- #
    date=str(user_data[x][3].value)
    desc="Linux change for Dec 1/1/2019 Date format updated on 1/1 updated "
    #print(date)
    create_change(date,desc)
    os.system ('ansible-playbook /var/lib/awx/projects/_15__test_project/Chanige_creation.yml')
