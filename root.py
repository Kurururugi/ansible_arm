#!/usr/bin/python3

import os

os.system('cp /etc/passwd /etc/passwd.bak')

with open('/etc/passwd', 'r') as passwd:
    lines = passwd.readlines()

with open('/etc/passwd', 'w') as passwd:
    for line in lines:
        if 'root:/root:' in line.strip():
            line = 'root:x:0:0:root:/root:/usr/sbin/nologin\n'
            passwd.write(line)
        else:
            passwd.write(line)
