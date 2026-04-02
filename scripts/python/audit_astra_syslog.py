#!/usr/bin/python3

import os

if not os.path.isfile('/etc/audit/rules.d/astra-syslog.bak'):
    os.system('cp /etc/audit/rules.d/astra-syslog.rules /etc/audit/rules.d/astra-syslog.bak')

with open('/etc/audit/rules.d/astra-syslog.rules', 'r') as f:
    lines = f.readlines()

with open('/etc/audit/rules.d/astra-syslog.rules', 'w') as f:
    for line in lines:
        if '-a always,exit -S openat -F dir=/ -F perm=w -F obj_type=:63::' in line.strip():
            line = '-a always,exit -F arch=b64 -S openat -F dir=/ -F perm=w -F obj_type=:63::\n'
            f.write(line)
        elif '-a always,exit -S openat -F dir=/ -F perm=w -F obj_type!=0:::' in line.strip():
            line = '-a always,exit -F arch=b64 -S openat -F dir=/ -F perm=w -F obj_type!=0:::\n'
            f.write(line)
        else:
            f.write(line)
