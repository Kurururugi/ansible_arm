#!/usr/bin/python3

import os
import configparser

class CustomConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

if not os.path.isfile('/etc/systemd/sleep.conf.bak'):
    os.system('cp /etc/systemd/sleep.conf /etc/systemd/sleep.conf.bak')

config = CustomConfigParser()
config.read('/etc/systemd/sleep.conf')

config.set('Sleep', 'AllowSuspend', 'no')
config.set('Sleep', 'AllowHibernation', 'no')
config.set('Sleep', 'AllowSuspendThenHibernate', 'no')
config.set('Sleep', 'AllowHybridSleep', 'no')

with open('/etc/systemd/sleep.conf', 'w') as configfile:
    config.write(configfile)

