#!/usr/bin/python3

import os
import configparser

class CustomConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

# create service for check raid status
if not os.path.isfile('/etc/systemd/system/raid_state.service'):
    os.system('touch /etc/systemd/system/raid_state.service')
    os.system('chmod 644 /etc/systemd/system/raid_state.service')
    config_service = CustomConfigParser()
    config_service.read('/etc/systemd/system/raid_state.service')
    config_service['Unit'] = {'Description': 'Check raid status',
                              'After': 'multi-user.target'}
    config_service['Service'] = {'ExecStart': '/usr/local/Project/RAID.sh'}
    with open('/etc/systemd/system/raid_state.service', 'w') as configfile:
        config_service.write(configfile)

# create timer for raid_state.service
if not os.path.isfile('/etc/systemd/system/raid_state.timer'):
    os.system('touch /etc/systemd/system/raid_state.timer')
    os.system('chmod 644 /etc/systemd/system/raid_state.timer')
    config_timer = CustomConfigParser()
    config_timer.read('/etc/systemd/system/raid_state.timer')
    config_timer['Unit'] = {'Description': 'Check raid status every 5 minutes'}
    config_timer['Timer'] = {'OnBootSec': '10s',
                             'OnUnitActiveSec': '300s',
                             'AccuracySec': '10s'}
    config_timer['Install'] = {'WantedBy': 'timers.target'}
    with open('/etc/systemd/system/raid_state.timer', 'w') as configfile:
        config_timer.write(configfile)

    os.system('systemctl daemon-reload')
    os.system('systemctl enable --now raid_state.timer')
