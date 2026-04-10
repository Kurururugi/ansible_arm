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

backup = '/lib/systemd/system/alpha.security.useractivity.service.bak'
with open(special_file, 'r') as src:
    with open(backup, 'w') as dest:
        dest.write(src.read())

config_useractivity = SystemdUnitParser()

config_useractivity.read(special_file)
if config_useractivity.has_section('Service'):
    config_useractivity.set('Service', 'User', 'operator_arm')
    config_useractivity.set('Service', 'Group', 'operator_arm')

with open(special_file, 'w') as f:
    config_useractivity.write(f)
