#!/usr/bin/python3

import os
from configupdater import ConfigUpdater


os.system('cp /etc/X11/fly-dm/fly-dmrc /etc/X11/fly-dm/fly-dmrc.bak')
config = ConfigUpdater()

config.read('/etc/X11/fly-dm/fly-dmrc')
config['X-*-Greeter']['NumLock'].value = 'On'
config['X-*-Greeter']['UserList'].value = 'true'
config['X-:0-Core']['AutoLoginEnable'].value = 'true'
config['X-:0-Core']['AutoLoginUser'].value = 'operator_arm'

with open('/etc/X11/fly-dm/fly-dmrc', 'w') as configfile:
    config.write(configfile)
