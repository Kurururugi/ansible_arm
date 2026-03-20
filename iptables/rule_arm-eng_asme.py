#!/usr/bin/python

import os

if not os.path.isdir('/etc/sysconfig'):
    os.system('mkdir /etc/sysconfig')
if not os.path.isfile('/etc/sysconfig/iptables'):
    os.system('touch /etc/sysconfig/iptables')

os.system('iptables -F')
os.system('iptables -F -t nat')
os.system('iptables -F -t mangle')
os.system('iptables -X')
os.system('iptables -t nat -X')
os.system('iptables -t mangle -X')
os.system('iptables -P INPUT DROP')
os.system('iptables -P OUTPUT DROP')
os.system('iptables -P FORWARD DROP')
os.system('iptables -A INPUT -i lo -j ACCEPT')
os.system('iptables -A OUTPUT -o lo -j ACCEPT')
os.system('iptables -A INPUT -p icmp --icmp-type echo-reply -j ACCEPT')
os.system('iptables -A INPUT -p icmp --icmp-type destination-unreachable -j DROP')
os.system('iptables -A INPUT -p icmp --icmp-type time-exceeded -j DROP')
os.system('iptables -A INPUT -p icmp --icmp-type echo-request -j ACCEPT')
os.system('iptables -A OUTPUT -p icmp -j ACCEPT')
os.system('iptables -A INPUT -p all -m state --state ESTABLISHED,RELATED -j ACCEPT')
os.system('iptables -A OUTPUT -p all -m state --state ESTABLISHED,RELATED -j ACCEPT')
os.system('iptables -A FORWARD -p all -m state --state ESTABLISHED,RELATED -j ACCEPT')
os.system('iptables -A INPUT -m state --state INVALID -j DROP')
os.system('iptables -A FORWARD -m state --state INVALID -j DROP')
os.system('iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP')
os.system('iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP')
os.system('iptables -A OUTPUT -p tcp ! --syn -m state --state NEW -j DROP')
os.system('iptables -A OUTPUT -p tcp --dport 123 -j ACCEPT')
os.system('iptables -A OUTPUT -p udp --dport 123 -j ACCEPT')
os.system('iptables -A INPUT -s 172.17.192.3/32 -p tcp -m multiport --dports 11000,11010,11020,11050 -j ACCEPT')
os.system('iptables -A INPUT -s 172.17.192.131/32 -p tcp -m multiport --dports 11000,11010,11020,11050 -j ACCEPT')
os.system('iptables -A INPUT -s 172.17.192.3/32 -p tcp -m multiport --dports 4572,4388,6551,6552,3388,4949,4950 -j ACCEPT')
os.system('iptables -A INPUT -s 172.17.192.131/32 -p tcp -m multiport --dports 4572,4388,6551,6552,3388,4949,4950 -j ACCEPT')
os.system('iptables -A INPUT -s 172.17.192.3/32 -p tcp -m multiport --dports 62544,389,15150,15151,3189 -j ACCEPT')
os.system('iptables -A INPUT -s 172.17.192.131/32 -p tcp -m multiport --dports 62544,389,15150,15151,3189 -j ACCEPT')
os.system('iptables -A INPUT -s 172.17.192.3/32 -p udp -m multiport --dports 161,162 -j ACCEPT')
os.system('iptables -A INPUT -s 172.17.192.131/32 -p udp -m multiport --dports 161,162 -j ACCEPT')
os.system('iptables -A INPUT -p tcp -m tcp --dport 22 -j DROP')

os.system('iptables -A OUTPUT -d 172.17.192.3/32 -p tcp -m multiport --dports 11000,11010,11020,11050 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.131/32 -p tcp -m multiport --dports 11000,11010,11020,11050 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.3/32 -p tcp -m multiport --dports 4572,4388,6551,6552,3388,4949,4950 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.131/32 -p tcp -m multiport --dports 4572,4388,6551,6552,3388,4949,4950 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.3/32 -p tcp -m multiport --dports 62544,389,15150,15151,3189 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.131/32 -p tcp -m multiport --dports 62544,389,15150,15151,3189 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.3/32 -p udp -m multiport --dports 161,162 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.131/32 -p udp -m multiport --dports 161,162 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.1/32 -p tcp -m tcp --dport 502 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.129/32 -p tcp -m tcp --dport 502 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.126/32 -p tcp -m tcp --dport 502 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.254/32 -p tcp -m tcp --dport 502 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.125/32 -p udp -m udp --dport 161 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.253/32 -p udp -m udp --dport 161 -j ACCEPT')

os.system('iptables -A OUTPUT -d 172.17.192.3/32 -p tcp -m tcp --dport 22 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.131/32 -p tcp -m tcp --dport 22 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.125/32 -p tcp -m tcp --dport 22 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.253/32 -p tcp -m tcp --dport 22 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.1/32 -p tcp -m multiport --dports 1740,1741,1742,1743 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.1/32 -p tcp -m multiport --dports 11740,11741,11742,11743 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.129/32 -p tcp -m multiport --dports 1740,1741,1742,1743 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.129/32 -p tcp -m multiport --dports 11740,11741,11742,11743 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.126/32 -p tcp -m multiport --dports 1740,1741,1742,1743 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.126/32 -p tcp -m multiport --dports 11740,11741,11742,11743 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.254/32 -p tcp -m multiport --dports 1740,1741,1742,1743 -j ACCEPT')
os.system('iptables -A OUTPUT -d 172.17.192.254/32 -p tcp -m multiport --dports 11740,11741,11742,11743 -j ACCEPT')

os.system('/sbin/iptables-save > /etc/sysconfig/iptables')

with open('/etc/network/interfaces', 'r') as f:
    content = f.readlines()
    check_iptables = False
    for line in content:
        if 'iptables-restore' in line:
            check_iptables = True

if check_iptables == False:
    with open ('/etc/network/interfaces', 'w') as f:
        for line in content:
            if 'iface lo inet' in line:
                line = 'iface lo inet loopback\npre-up iptables-restore < /etc/sysconfig/iptables\n'
                f.write(line)
            else:
                f.write(line)
