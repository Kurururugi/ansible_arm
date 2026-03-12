#!/usr/bin/python3

import os

#create users

os.system('useradd -m -c "asutp operator" operator_arm')
os.system('usermod --password $(echo "Bzpa/12345" | openssl passwd -1 -stdin) operator_arm')
os.system('usermod -G "" operator_arm')

os.system('faillog -u operator_arm -m 50')
os.system('faillog -u curator -m 50')
