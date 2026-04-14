#!/usr/bin/python3

import os

if not os.path.isfile('/etc/sysctl.d/999-astra.conf.bak'):
    os.system('cp /etc/sysctl.d/999-astra.conf /etc/sysctl.d/999-astra.conf.bak')

with open('/etc/sysctl.d/999-astra.conf', 'r') as f:
    old_data = f.readlines()

already_exist_ipv6 = False
for line in old_data:
    if 'net.ipv6.conf.all.disable_ipv6' in line.strip():
        already_exist_swap = True

if not already_exist_ipv6:
    os.system('echo "net.ipv6.conf.all.disable_ipv6 = 1" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv6.conf.default.disable_ipv6 = 1" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.ip_forward=0" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.all.send_redirects=0" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.default.send_redirects=0" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.all.accept_source_route = 0" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.default.accept_source_route = 0" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.all.accept_redirects = 0" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.default.accept_redirects = 0" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.all.secure_redirects = 0" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.default.secure_redirects = 0" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.all.log_martians = 1" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.default.log_martians = 1" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.icmp_echo_ignore_broadcasts = 1" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.icmp_ignore_bogus_error_responses = 1" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.all.rp_filter = 1" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.conf.default.rp_filter = 1" >> /etc/sysctl.d/999-astra.conf')
    os.system('echo "net.ipv4.tcp_syncookies = 1" >> /etc/sysctl.d/999-astra.conf')


if not os.path.isfile('/etc/hosts.bak'):
    os.system('cp /etc/hosts /etc/hosts.bak')
with open('/etc/hosts', 'r') as f:
    lines = f.readlines()
with open('/etc/hosts', 'w') as f:
    for line in lines:
        if '::' in line.strip():
            f.write('# ' + line)
        else:
            f.write(line)
