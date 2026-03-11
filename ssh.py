#!/usr/bin/python3

import os

os.system('cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak')

aleady_exist = False

with open("/etc/ssh/sshd_config", "r") as f:
    lines = f.readlines()
with open("/etc/ssh/sshd_config", "w") as f:
    for line in lines:
        if 'ClientAliveInterval' in line.strip():
            line = 'ClientAliveInterval 600\n'
            f.write(line)
        elif 'ClientAliveCountMax' in line.strip():
            line = 'ClientAliveCountMax 3\n'
            f.write(line)
        elif 'AllowUsers administrator' in line.strip():
            aleady_exist = True
            f.write(line) 
        else:
            f.write(line)

if not aleady_exist:
   os.system('echo "\nAllowUsers administrator" >> /etc/ssh/sshd_config')
   os.system('echo "PermitRootLogin no" >> /etc/ssh/sshd_config')

   os.system('cp /etc/bash.bashrc /etc/bash.bashrc.bak')
   os.system('echo "\nTMOUT=1800" >> /etc/bash.bashrc')
   os.system('echo "readonly TMOUT" >> /etc/bash.bashrc')
   os.system('echo "export TMOUT" >> /etc/bash.bashrc')

os.system('systemctl restart ssh')
