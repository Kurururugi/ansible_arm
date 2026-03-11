#!/usr/bin/python3

import os
import configparser

class CustomConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

if not os.path.isdir('/root/.config/'):
    os.system('mkdir /root/.config/')
if not os.path.isdir('/root/.config/rusbitech/'):
    os.system('mkdir /root/.config/rusbitech/')
if not os.path.isfile('/root/.config/rusbitech/fly-astra-update.conf'):
    os.system('touch /root/.config/rusbitech/fly-astra-update.conf')
os.system('cp /root/.config/rusbitech/fly-astra-update.conf /root/.config/rusbitech/fly-astra-update.conf.bak')
config = CustomConfigParser()
config.read('/root/.config/rusbitech/fly-astra-update.conf')
config['General'] = {'AutoUpdate': 'false',
                     'ExpertMode': 'true',
                     'GostCheck': 'false',
                     'IsCrashed': 'false',
                     'KeepSrc': 'false',
                     'Md5Check': 'false',
                     'NoMainRepo': 'false',
                     'SetupWidth': '536',
                     'Snapshot': 'false',
                     'Sources': '@Invalid()',
                     'UseRepo': 'false'}

config['FlyGeometry'] = {'frame_height': '674',
                         'frame_width': '560',
                         'frame_x': '0',
                         'frame_y': '0',
                         'fullscreen': 'false',
                         'height': '635',
                         'maximized': 'false',
                         'screen': '0',
                         'width': '548',
                         'x': '6',
                         'y': '33'}

with open('/root/.config/rusbitech/fly-astra-update.conf', 'w') as configfile:
    config.write(configfile)
