#!/usr/bin/python3

import os
from lxml import etree

if not os.path.isfile('/opt/Automiq/Alpha.Security/alpha.security.ic.xml.bak'):
    os.system('cp /opt/Automiq/Alpha.Security/alpha.security.ic.xml /opt/Automiq/Alpha.Security/alpha.security.ic.xml.bak')

parser = etree.XMLParser(remove_comments=False)
tree = etree.parse('/opt/Automiq/Alpha.Security/alpha.security.ic.xml', parser)
root = tree.getroot()

iclist = root.find('ICList')
iclist.clear()
iclist.text = '\n                '

exclude_list = root.find('ICExclude')
exclude_list.clear()
exclude_list.text = '\n                '

control_files = ['/boot/grub/grub.cfg',
                 '/etc/X11/default-display-manager',
                 '/etc/fstab',
                 '/etc/group',
                 '/etc/pam.conf',
                 '/etc/pam.d/',
                 '/etc/passwd',
                 '/etc/security',
                 '/etc/shells',
                 '/etc/sysctl.conf',
                 '/lib/modules',
                 '/lib/security/',
                 '/sbin/',
                 '/bin/',
                 '/usr/bin/',
                 '/usr/sbin/',
                 '/etc/init.d/']

exclude_files = ['/opt/FSControl',
                 '/usr/bin/X11/',
                 '/bin/X11/']

for i, file in enumerate(control_files):
    new_icfile = etree.SubElement(iclist, 'IC')
    new_icfile.set('file', file)
    if i < len(control_files) - 1:
        new_icfile.tail = '\n                '
    else:
        new_icfile.tail = '\n        '
iclist.tail = '\n        '

for i, file in enumerate(exclude_files):
    new_exfile = etree.SubElement(exclude_list, 'IC')
    new_exfile.set('file', file)
    if i < len(exclude_files) - 1:
        new_exfile.tail = '\n                '
    else:
        new_exfile.tail = '\n        '
exclude_list.tail = '\n        '

tree.write('/opt/Automiq/Alpha.Security/alpha.security.ic.xml',
           encoding='utf-8',
           xml_declaration=False,
           pretty_print=True)
