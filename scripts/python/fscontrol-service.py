#!/usr/bin/python3

import os
from SystemdUnitParser import SystemdUnitParser

path = '/etc/systemd/system/FSControl.service'
backup = '/etc/systemd/system/FSControl.service.bak'
with open(path, 'r') as src:
    with open(backup, 'w') as dest:
        dest.write(src.read())

config = SystemdUnitParser()

config.read(path)
if config.has_section('Service'):
    config.set('Service', 'ExecStart', '/opt/FSControl/dotnet /opt/FSControl/FSControl.WorkerWeb.dll')

with open(path, 'w') as f:
    config.write(f)
