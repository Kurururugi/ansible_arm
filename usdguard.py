#!/usr/bin/python3

import os


os.system('cp /lib/systemd/system/usbguard.service /lib/systemd/system/usbguard.service.bak')

with open('/lib/systemd/system/usbguard.service', 'r') as f:
    old_data = f.readlines()

already_exist = False
for line in old_data:
    if 'ExecStartPre = /bin/sleep 10' in line.strip():
        already_exist = True

if not already_exist:
    with open('/lib/systemd/system/usbguard.service', 'w') as f:
        for line in old_data:
            if 'DevicePolicy' in line.strip():
                line = 'DevicePolicy = closed\n' + 'ExecStartPre = /bin/sleep 10\n'
                f.write(line)
            else:
                f.write(line)

    os.system('systemctl daemon-reload')
    os.system('systemctl restart usbguard.service')

