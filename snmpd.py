#!/usr/bin/python3

import os
import configparser

#/etc/snmp/snmpd.conf
os.system('cp /etc/snmp/snmpd.conf /etc/snmp/snmpd.conf.bak')
#Comment all lines
with open('/etc/snmp/snmpd.conf', 'r') as f:
    content = f.readlines()
with open('/etc/snmp/snmpd.conf', 'w') as f:
    for line in content:
        if line[0] != '#':
            f.write('#' + line)
        else:
            f.write(line)
#Add new lines
os.system('echo "agentAddress udp:161" >> /etc/snmp/snmpd.conf')
os.system('echo "createUser SEMMonitor SHA SEMAuth/12345" >>  /etc/snmp/snmpd.conf')
os.system('echo "group SEMGROUP usm SEMMonitor" >>  /etc/snmp/snmpd.conf')
os.system('echo "view viewall included .1.3.6" >>  /etc/snmp/snmpd.conf')
os.system('''echo 'access SEMGROUP "" usm authnopriv exact viewall viewall none' >>  /etc/snmp/snmpd.conf''')
os.system('echo "rouser SEMMonitor" >>  /etc/snmp/snmpd.conf')


#/lib/systemd/system/snmpd.service
class CustomConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr

os.system('cp /lib/systemd/system/snmpd.service /lib/systemd/system/snmpd.service_bak')
config = CustomConfigParser()
config.read('/lib/systemd/system/snmpd.service')
config.set('Service', 'ExecStart', '/usr/sbin/snmpd -LSwd -Lf /dev/null -u Debian-snmp -g Debian-snmp -I -smux,mteTrigger,mteTriggerConf -f -p /run/snmpd.pid')
with open('/lib/systemd/system/snmpd.service', 'w') as configfile:
	config.write(configfile)

os.system('systemctl daemon-reload')
os.system('systemctl restart snmpd.service')

