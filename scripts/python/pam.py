#!/usr/bin/python3

import os

# backup /etc/pam.d/common-password
if not os.path.isfile('/etc/pam.d/common-password.bak'):
    os.system('cp /etc/pam.d/common-password /etc/pam.d/common-password.bak')

with open('/etc/pam.d/common-password', 'r') as f:
    lines = f.readlines()
with open('/etc/pam.d/common-password', 'w') as f:
    for line in lines:
        if 'pam_pwquality.so' in line.strip():
            line = 'password        requisite                       pam_pwquality.so retry=3 minlen=10'
            line = line + ' difok=5 maxsequence=3 maxrepeat=2 minclass=3 gecoscheck=1 enforce_for_root usercheck=1\n'
            f.write(line)
        else:
            f.write(line)

# backup /etc/pam.d/common-auth
if not os.path.isfile('/etc/pam.d/common-auth.bak'):
    os.system('cp /etc/pam.d/common-auth /etc/pam.d/common-auth.bak')

with open('/etc/pam.d/common-auth', 'r') as f:
    lines = f.readlines()
with open('/etc/pam.d/common-auth', 'w') as f:
    for line in lines:
        if 'pam_succeed_if.so' in line.strip():
            line = '# ' + line
            f.write(line)
        elif 'pam_faillock.so preauth' in line.strip():
            line = 'auth    requisite			'
            line = line + 'pam_faillock.so preauth audit per_user deny=10 unlock_time=1800\n'
            f.write(line)
        elif 'pam_faillock.so authfail' in line.strip():
            line = 'auth    required			'
            line = line + 'pam_faillock.so authfail audit per_user deny=10 unlock_time=1800\n'
            f.write(line)
        else:
            f.write(line)

# backup /etc/pam.d/su
if not os.path.isfile('/etc/pam.d/su.bak'):
    os.system('cp /etc/pam.d/su /etc/pam.d/su.bak')

with open('/etc/pam.d/su', 'r') as f:
    lines = f.readlines()
with open('/etc/pam.d/su', 'w') as f:
    checked = False
    for line in lines:
        if ('pam_wheel.so' in line.strip()) and checked != True:
            checked = True
            line = 'auth       required pam_wheel.so use_uid\n'
            f.write(line)
        else:
            f.write(line)

