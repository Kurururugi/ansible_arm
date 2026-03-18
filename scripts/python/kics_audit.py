#!/usr/bin/python3

import os

if not os.path.isfile('/etc/audit/rules.d/kaspersky.rules.bak'):
    os.system('cp /etc/audit/rules.d/kaspersky.rules /etc/audit/rules.d/kaspersky.rules.bak')

with open("/etc/audit/rules.d/kaspersky.rules", "r") as f:
    lines = f.readlines()
with open("/etc/audit/rules.d/kaspersky.rules", "w") as f:
    for line in lines:
        if 'always' in line.strip():
            line = '# ' + line
            f.write(line)
        else:
            f.write(line)
