#!/usr/bin/python3

import os
import socket
import fcntl
import struct

#/etc/chrony/chrony.conf
os.system('cp /etc/chrony/chrony.conf /etc/chrony/chrony.conf_bak')

#ip_addr = socket.gethostbyname(socket.gethostname())

#s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#s.connect(("172.16.1.30", 80))
#ip_addr = s.getsockname()[0]

interface_name = 'eth0'
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_addr = socket.inet_ntoa(fcntl.ioctl(
	s.fileno(),
	0x8915,  # SIOCGIFADDR
	struct.pack('256s', interface_name[:15].encode())
)[20:24])

octets = ip_addr.split('.')

if octets[2][0] == '2':
	ntp_server_1 = '192.168.' + octets[2] + '.14'
	ntp_server_2 = '192.168.' + octets[2] + '.142'
elif octets[2] == '192':
	ntp_server_1 = '172.17.192.126'
	ntp_server_2 = '172.17.192.254'
else:
	ntp_server_1 = '172.16.0.6'
	ntp_server_2 = '172.16.1.6'

with open("/etc/chrony/chrony.conf", "r") as f:
    lines = f.readlines()
with open("/etc/chrony/chrony.conf", "w") as f:
    for line in lines:
        if 'makestep 1 3' in line.strip():
            line = 'makestep 1 -1\n'
            f.write(line)
        elif 'Debian vendor zone.' in line.strip():
            line = ('# Use Debian vendor zone.\nserver ' + str(ntp_server_1)  
            + ' iburst minpoll 1 maxpoll 2 prefer trust\nserver ' + str(ntp_server_2)  
            + ' iburst minpoll 1 maxpoll 2 trust')
            f.write(line)
        elif ('pool' not in line.strip()) and ('server' not in line.strip()):
            f.write(line)

os.system('systemctl restart chrony.service')
