#!/usr/bin/python3

import os

path = '/lib/systemd/system/'
files = os.listdir(path)

for file in files:
   if 'alpha' in file:
      with open('/lib/systemd/system/' + file, 'r') as f:
         lines = f.readlines()
      with open('/lib/systemd/system/' + file, 'w') as f:
         for line in lines:
            if 'User' in line:
               line = 'User=start_hmi\n'
               f.write(line)
            elif 'Group' in line:
               line = 'Group=start_hmi\n'
               f.write(line)
            else:
               f.write(line)

with open('/lib/systemd/system/alpha.security.useractivity.service', 'r') as f:
   lines = f.readlines()
with open('/lib/systemd/system/alpha.security.useractivity.service', 'w') as f:
   for line in lines:
      if 'User' in line:
         line = 'User=operator_arm\n'
         f.write(line)
      elif 'Group' in line:
         line = 'Group=operator_arm\n'
         f.write(line)
      else:
         f.write(line)
