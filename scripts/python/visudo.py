#!/usr/bin/python3

import os

if not os.path.isfile('/etc/sudoers'):
    os.system('cp /etc/sudoers /etc/sudoers.bak')

with open('/etc/sudoers', 'r') as f:
    first_line = f.readline()
    if '#Cmnd_Alias SHELLS = /bin/sh, /bin/bash, /bin/zsh, /usr/bin/zsh, /usr/bin/bash' in first_line:
        already_exist = True
    else:
        already_exist = False

if not already_exist:
    with open('/etc/sudoers', 'r+') as f:
        data = f.read()
        f.seek(0)
        f.write(
            '#Cmnd_Alias SHELLS = /bin/sh, /bin/bash, /bin/zsh, /usr/bin/zsh, /usr/bin/bash\n'
            + 'Defaults	iolog_dir=/var/log/sudo-io/%{user}\n'
            + data
            )
        f.write('Defaults timestamp_timeout=30\n')
        f.write('#ALL ALL=(ALL:ALL) !SHELLS\n')


    with open('/etc/sudoers', 'r') as f:
        lines = f.readlines()

    with open('/etc/sudoers', 'w') as f:
        for line in lines:
            if '%astra-admin' in line:
                line = '%astra-admin ALL=(ALL:ALL) LOG_INPUT: LOG_OUTPUT: ALL\n'
                f.write(line)
            else:
                f.write(line)
