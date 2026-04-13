#!/usr/bin/python3

import os
import glob
from SystemdUnitParser import SystemdUnitParser

pattern = '/lib/systemd/system/alpha.*'
service_files  = glob.glob(pattern)
service_files = [f for f in service_files if f.endswith('.service')]

special_file = '/lib/systemd/system/alpha.security.useractivity.service'
service_files = [f for f in service_files if f != special_file]

for file in service_files:
    backup = f"{file}.bak"
    with open(file, 'r') as src:
        with open(backup, 'w') as dest:
            dest.write(src.read())

    config = SystemdUnitParser()

    config.read(file)
    if config.has_section('Service'):
        config.set('Service', 'User', 'start_hmi')
        config.set('Service', 'Group', 'start_hmi')

    with open(file, 'w') as f:
        config.write(f)

backup = '/opt/Automiq/Alpha.Security/alpha.security.useractivity.sh.bak'
with open('/opt/Automiq/Alpha.Security/alpha.security.useractivity.sh', 'r') as src:
    with open(backup, 'w') as dest:
        dest.write(src.read())

with open('/opt/Automiq/Alpha.Security/alpha.security.useractivity.sh', 'r') as f:
    data = f.readlines()
with open('/opt/Automiq/Alpha.Security/alpha.security.useractivity.sh', 'w') as f:
    for line in data:
        if 'export XAUTHORITY' in line:
            line = 'export XAUTHORITY="/home/operator_arm/.Xauthority"\n'
        elif '/opt/Automiq/Alpha.Security/' in line:
            line = '/opt/Automiq/Alpha.Security/alpha.security.useractivity 2>/dev/null\n'
        f.write(line)
