#!/usr/bin/python3

import os
import configparser

class CustomConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

if not os.path.isfile('/etc/fly-kiosk/.config/lockerrc/lockerrc.bak'):
    os.system('cp /etc/fly-kiosk/.config/lockerrc/lockerrc /etc/fly-kiosk/.config/lockerrc/lockerrc.bak')

config = CustomConfigParser()
config.read('/etc/fly-kiosk/.config/lockerrc/lockerrc')
config.set('Variables', 'LockerOnSleep', 'false')
config.set('Variables', 'LockerOnDPMS', 'false')
config.set('Variables', 'LockerOnLid', 'false')
config.set('Variables', 'LockerOnSwitch', 'false')
config.set('Variables', 'ScreenSaverDelay', '0')

with open('/etc/fly-kiosk/.config/lockerrc/lockerrc', 'w') as configfile:
    config.write(configfile)

