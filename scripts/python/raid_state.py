#!/usr/bin/python3

from os import system
from SystemdUnitParser import SystemdUnitParser

# create service for check raid status

config_service = SystemdUnitParser()

config_service.add_section('Unit')
config_service.add_section('Service')

config_service.set('Unit', 'Description', 'Check raid status')
config_service.set('Unit', 'After', 'multi-user.target')
config_service.set('Service', 'ExecStart', '/usr/local/Project/RAID.sh')

with open('/etc/systemd/system/raid_state.service', 'w') as service:
    config_service.write(service)

# create timer for raid_state.service

config_timer = SystemdUnitParser()

config_timer.add_section('Unit')
config_timer.add_section('Timer')
config_timer.add_section('Install')

config_timer.set('Unit', 'Description', 'Check raid status every 5 minutes')
config_timer.set('Timer', 'OnBootSec', '10s')
config_timer.set('Timer', 'OnUnitActiveSec', '300s')
config_timer.set('Timer', 'AccuracySec', '10s')
config_timer.set('Install', 'WantedBy', 'timers.target')

system('systemctl daemon-reload')
system('systemctl enable --now raid_state.timer')
