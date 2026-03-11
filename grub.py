#!/usr/bin/python3

import os

os.system('cp /etc/default/grub /etc/default/grub.bak')

with open("/etc/default/grub", "r") as f:
    lines = f.readlines()
with open("/etc/default/grub", "w") as f:
    for line in lines:
        if 'GRUB_TIMEOUT' in line.strip():
            line = 'GRUB_TIMEOUT=0\n'
            f.write(line)
        else:
            f.write(line)

os.system('update-grub')
