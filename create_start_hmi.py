#!/usr/bin/python3

import os
import re

os.system('adduser start_hmi --system --group --no-create-home')
with open('/etc/passwd', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if 'start_hmi' in line.strip():
            user_string = re.findall("\d+", line)
            user_number = user_string[1]
            break

if not os.path.isfile('/etc/sysctl.d/99-allow-ping.conf'):
    os.system('touch /etc/sysctl.d/99-allow-ping.conf')
with open('/etc/sysctl.d/99-allow-ping.conf', 'w') as f:
    f.write('net.ipv4.ping_group_range = ' + str(user_number) + ' ' + str(user_number))
os.system('sysctl --system')
