#!/usr/bin/python3

import os
from configupdater import ConfigUpdater

os.system('cp /usr/share/fly-wm/theme/default.themerc /usr/share/fly-wm/theme/default.themerc.bak')
config = ConfigUpdater()
config.read('/usr/share/fly-wm/theme/default.themerc')
config['Variables']['PingWindowTime'].value = '15000'
config['Variables']['LockerOnLid'].value = 'false'
config['Variables']['ScreenSaverDelay'].value = '0'
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

with open('/usr/share/fly-wm/theme/default.themerc', 'w') as configfile:
    config.write(configfile)

os.system('cp /usr/share/fly-wm/theme/default.themerc.fly-kiosk /usr/share/fly-wm/theme/default.themerc.fly-kiosk.bak')
config.read('/usr/share/fly-wm/theme/default.themerc.fly-kiosk')
config['Variables']['PingWindowTime'].value = '15000'
config['Variables']['LockerOnLid'].value = 'false'
config['Variables']['ScreenSaverDelay'].value = '0'
config['Variables']['LockerOnDPMS'].value = 'false'
config['Variables']['LockerOnSleep'].value = 'false'
config['Variables']['LockerOnSwitch'].value = 'false'
config['Variables']['LockerTTYLock'].value = 'true'
config['Variables']['LockerXaccessLock'].value = 'true'
config['Variables']['LockerShowUsername'].value = 'true'
config['Variables']['numLockOn'].value = 'true'
config['Variables']['AltMouseOps'].value = 'false'
config['Variables']['TitlebarColor'].value = '#118bcc'
config['Variables']['TitlebarColor2'].value = '#118bcc'
config['Variables']['TitleStringColor'].value = '#ffffff'
config['Variables']['FrameColor'].value = '#118bcc'

with open('/usr/share/fly-wm/theme/default.themerc.fly-kiosk', 'w') as configfile:
    config.write(configfile)
