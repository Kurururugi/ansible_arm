#!/usr/bin/python3

import os

#/etc/apt/sources.list
os.system('cp /etc/apt/sources.list /etc/apt/sources.list.bak')
#Comment all lines
with open('/etc/apt/sources.list', 'r') as f:
   content = f.readlines()
with open('/etc/apt/sources.list', 'w') as f:
   for line in content:
      if line[0] != '#':
         f.write('#' + line)
      else:
         f.write(line)

os.system('echo "\ndeb file:///usr/local/alse/iso/ 1.8_x86-64 contrib main non-free" >> /etc/apt/sources.list')
os.system('apt update')
