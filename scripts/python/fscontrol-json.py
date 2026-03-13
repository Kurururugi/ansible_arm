#!/usr/bin/python3

import json
import os

if not os.path.isfile('/opt/FSControl/appsettings_unix.json'):
    os.system('cp /opt/FSControl/appsettings_unix.json /opt/FSControl/appsettings_unix.json.bak')

with open('/opt/FSControl/appsettings_unix.json') as f:
    data = json.load(f)

data["adminGroup"] = "fscontrol"
data["extensions"] = [""]
data["pathForControl"] = [
    "/boot/vmlinuz-*",
    "/boot/initrd.img-*",
    "/boot/grub/grub.cfg",
    "/etc/X11/default-display-manager",
    "/etc/fstab",
    "/etc/group",
    "/etc/pam.conf",
    "/etc/pam.d/*",
    "/etc/passwd",
    "/etc/rc*",
    "/etc/security",
    "/etc/shells",
    "/etc/sysctl.conf",
    "/lib/modules/*/misk/digsig_verif.ko",
    "/lib/modules/*/misk/parsec.ko",
    "/lib/modules/*/misk/parsec-cifs.ko",
    "/lib/security/",
    "/sbin/",
    "/bin/",
    "/usr/bin/",
    "/usr/sbin/",
    "/etc/init.d/*"
    ]
data["pathForIgnore"] = [
    "/opt/FSControl",
    "/usr/bin/X11/*",
    "/bin/X11/"
    ]
with open('/opt/FSControl/appsettings_unix.json', 'w') as f:
    json.dump(data, f, indent=4)
