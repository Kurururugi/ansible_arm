#!/usr/bin/python3

import os
from configparser import ConfigParser


if not os.path.isfile('/etc/xdg/rusbitech/fly-vkbd.conf'):
    os.system('touch /etc/xdg/rusbitech/fly-vkbd.conf')

config = ConfigParser()
config.optionxform = str
config.read('/etc/xdg/rusbitech/fly-vkbd.conf')
config['General'] = {'buttonMenu':'false'}

with open('/etc/xdg/rusbitech/fly-vkbd.conf', 'w') as configfile:
    config.write(configfile)
