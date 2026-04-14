#!/usr/bin/python3

import os


if not os.path.isfile('/etc/logrotate.d/audit'):
    os.system('touch /etc/logrotate.d/audit')

os.system('echo "/var/log/audit/audit.log"                 > /etc/logrotate.d/audit')
os.system('echo "{"                                        >> /etc/logrotate.d/audit')
os.system('echo "postrotate"                               >> /etc/logrotate.d/audit')
os.system('echo "  invoke-rc.d auditd restart > /dev/null" >> /etc/logrotate.d/audit')
os.system('echo "endscript "                               >> /etc/logrotate.d/audit')
os.system('echo "}"                                        >> /etc/logrotate.d/audit')

os.system('cp /etc/logrotate.d/syslog-ng /etc/logrotate.d/syslog-ng.bak')

with open('/etc/logrotate.d/syslog-ng', 'r') as f:
    lines = f.readlines()

with open('/etc/logrotate.d/syslog-ng', 'w') as f:
    for line in lines:
        if '/var' in line:
            f.write(line)

with open('/etc/logrotate.d/syslog-ng', 'r') as f:
    lines = f.readlines()

with open('/etc/logrotate.d/syslog-ng', 'w') as f:
    for line in lines:
        if '/var/log/syslog' in line:
            f.write(line
                + "{\n"
                + "postrotate\n"
                + "  syslog-ng-ctl reopen > /dev/null\n"
                + "endscript\n"
                + "}\n"
                )
        elif '/var/log/error' in line:
            f.write(line
                + "{\n"
                + "sharedscripts\n"
                + "postrotate\n"
                + "  syslog-ng-ctl reopen > /dev/null\n"
                + "endscript\n"
                + "}\n"
                )
        else:
            f.write(line)
