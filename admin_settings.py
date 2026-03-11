#!/usr/bin/python3

import os
from configupdater import ConfigUpdater

os.system('cp /home/administrator/.fly/theme/default.themerc /home/administrator/.fly/theme/default.themerc.bak')
config = ConfigUpdater()
config.read('/home/administrator/.fly/theme/default.themerc')
config['Variables']['PingWindowTime'].value = '15000'
config['Variables']['LockerOnLid'].value = 'true'
config['Variables']['ScreenSaverDelay'].value = '600'
config['Variables']['LockerOnDPMS'].value = 'false'
config['Variables']['LockerOnSleep'].value = 'false'
config['Variables']['LockerOnSwitch'].value = 'false'
config['Variables']['LockerTTYLock'].value = 'true'
config['Variables']['LockerXaccessLock'].value = 'true'
config['Variables']['LockerShowUsername'].value = 'true'
config['Variables']['numLockOn'].value = 'true'
config['Variables']['AltMouseOps'].value = 'false'
config['Variables']['TitlebarColor'].value = 'PrimaryColor'
config['Variables']['TitlebarColor2'].value = 'PrimaryColor'
config['Variables']['TitleStringColor'].value = 'PrimaryTextColor'
config['Variables']['FrameColor'].value = 'PrimaryColor'

with open('/home/administrator/.fly/theme/default.themerc', 'w') as configfile:
    config.write(configfile)

os.system('cp /home/administrator/.fly/theme/current.themerc /home/administrator/.fly/theme/current.themerc.bak')
config.read('/home/administrator/.fly/theme/current.themerc')
config['Variables']['PingWindowTime'].value = '15000'
config['Variables']['LockerOnLid'].value = 'true'
config['Variables']['ScreenSaverDelay'].value = '600'
config['Variables']['LockerOnDPMS'].value = 'false'
config['Variables']['LockerOnSleep'].value = 'false'
config['Variables']['LockerOnSwitch'].value = 'false'
config['Variables']['LockerTTYLock'].value = 'true'
config['Variables']['LockerXaccessLock'].value = 'true'
config['Variables']['LockerShowUsername'].value = 'true'
config['Variables']['numLockOn'].value = 'true'
config['Variables']['AltMouseOps'].value = 'false'
config['Variables']['TitlebarColor'].value = 'PrimaryColor'
config['Variables']['TitlebarColor2'].value = 'PrimaryColor'
config['Variables']['TitleStringColor'].value = 'PrimaryTextColor'
config['Variables']['FrameColor'].value = 'PrimaryColor'

with open('/home/administrator/.fly/theme/current.themerc', 'w') as configfile:
    config.write(configfile)

os.system('cp /home/administrator/.fly/theme/default.themerc.fly-kiosk /home/administrator/.fly/theme/default.themerc.fly-kiosk.bak')
config.read('/home/administrator/.fly/theme/default.themerc.fly-kiosk')
config['Variables']['PingWindowTime'].value = '15000'
config['Variables']['LockerOnLid'].value = 'true'
config['Variables']['ScreenSaverDelay'].value = '600'
config['Variables']['LockerOnDPMS'].value = 'false'
config['Variables']['LockerOnSleep'].value = 'false'
config['Variables']['LockerOnSwitch'].value = 'false'
config['Variables']['LockerTTYLock'].value = 'true'
config['Variables']['LockerXaccessLock'].value = 'true'
config['Variables']['LockerShowUsername'].value = 'true'
config['Variables']['numLockOn'].value = 'true'
config['Variables']['AltMouseOps'].value = 'false'
config['Variables']['TitlebarColor'].value = 'PrimaryColor'
config['Variables']['TitlebarColor2'].value = 'PrimaryColor'
config['Variables']['TitleStringColor'].value = 'PrimaryTextColor'
config['Variables']['FrameColor'].value = 'PrimaryColor'

with open('/home/administrator/.fly/theme/default.themerc.fly-kiosk', 'w') as configfile:
    config.write(configfile)

