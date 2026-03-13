#!/usr/bin/python3

import os

os.system('cp /etc/usbguard/rules.conf /etc/usbguard/rules.conf.bak')

with open('/etc/usbguard/rules.conf', 'r') as usb_rule:
    rules = usb_rule.readlines()

already_exist = False
for line in rules:
    if 'Guardant Sign' in line.strip():
        already_exist = True

if not already_exist:
    with open('/etc/usbguard/rules.conf', 'a') as usb_rule:
        usb_rule.write('allow id 17ef:608d serial "" name "lenovo USB Optical Mouse"\n')
        usb_rule.write('allow id 413c:2113 serial "" name "Dell KB216 Wired Keyboard"\n')
        usb_rule.write('allow id 0a89:00c2 serial "" name "Guardant Sign"\n')
        usb_rule.write('allow id 046d:c34b serial "" name "USB Keyboard"\n')
        usb_rule.write('allow id 046d:c077 serial "" name "USB Optical Mouse"\n')
        usb_rule.write('allow id 8564:1000 serial "796Q7W8ROV1GBVLA" name "Mass Storage Device"\n')
        os.system('systemctl restart usbguard')
