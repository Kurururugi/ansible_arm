#!/usr/bin/python3

import os

if not os.path.isfile('/etc/systemd/system/FSControl.service.bak'):
    os.system('cp /etc/systemd/system/FSControl.service /etc/systemd/system/FSControl.service.bak')

with open("/etc/systemd/system/FSControl.service", "r") as f:
    lines = f.readlines()

with open("/etc/systemd/system/FSControl.service", "w") as f:
    for line in lines:
        if 'ExecStart' in line.strip():
            line = 'ExecStart=/opt/FSControl/dotnet /opt/FSControl/FSControl.WorkerWeb.dll\n'
            f.write(line)
        else:
            f.write(line)
