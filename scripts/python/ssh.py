#!/usr/bin/python3

import os

if not os.path.isfile('/etc/ssh/sshd_config.bak'):
    os.system('cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak')

aleady_exist = False

with open("/etc/ssh/sshd_config", "r") as f:
    lines = f.readlines()
with open("/etc/ssh/sshd_config", "w") as f:
    for line in lines:
        if 'X11Forwarding' in line.strip():
            line = 'X11Forwarding no\n'
            f.write(line)
        elif 'AllowUsers administrator' in line.strip():
            aleady_exist = True
            f.write(line) 
        else:
            f.write(line)

if not aleady_exist:
    os.system('echo "\nAllowUsers administrator" >> /etc/ssh/sshd_config')
    os.system('echo "PermitRootLogin no" >> /etc/ssh/sshd_config')
    os.system('echo "ClientAliveInterval 1800" >> /etc/ssh/sshd_config')
    os.system('echo "ClientAliveCountMax 0" >> /etc/ssh/sshd_config')
    os.system('echo "Protocol 2" >> /etc/ssh/sshd_config')
    os.system('echo "MaxAuthTries 3" >> /etc/ssh/sshd_config')
    os.system('echo "MACs hmac-sha2-512-etm@openssh.com,hmac-sha2-256-etm@openssh.com,umac-128-etm@openssh.com,hmac-sha2-512,hmac-sha2-256,umac-128@openssh.com" >> /etc/ssh/sshd_config')

    if not os.path.isfile('/etc/bash.bashrc.bak'):
        os.system('cp /etc/bash.bashrc /etc/bash.bashrc.bak')
    os.system('echo "\nTMOUT=1800" >> /etc/bash.bashrc')
    os.system('echo "readonly TMOUT" >> /etc/bash.bashrc')
    os.system('echo "export TMOUT" >> /etc/bash.bashrc')

os.system('systemctl restart ssh')
