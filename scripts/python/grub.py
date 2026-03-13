#!/usr/bin/python3

import os

if not os.path.isfile('/etc/default/grub.bak'):
    os.system('cp /etc/default/grub /etc/default/grub.bak')

with open("/etc/default/grub", "r") as f:
    lines = f.readlines()
with open("/etc/default/grub", "w") as f:
    for line in lines:
        if 'GRUB_TIMEOUT' in line.strip():
            line = 'GRUB_TIMEOUT=0\n'
            f.write(line)
        elif 'GRUB_CMDLINE_LINUX_DEFAULT=' in line.strip():
            line = 'GRUB_CMDLINE_LINUX_DEFAULT="splash quiet parsec.mac=0 net.ifnames=0 ipv6.disable=1 audit=1"\n'
            f.write(line)
        else:
            f.write(line)

os.system('''echo '\nGRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX init_on_alloc=1"'                              >> /etc/default/grub''')
os.system('''echo 'GRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX slab_nomerge"'                                   >> /etc/default/grub''')
os.system('''echo 'GRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX iommu=force iommu.strict=1 iommu.passthrough=0"' >> /etc/default/grub''')
os.system('''echo 'GRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX randomize_kstack_offset=1"'                      >> /etc/default/grub''')
os.system('''echo 'GRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX mitigations=auto,nosmt"'                         >> /etc/default/grub''')
os.system('''echo 'GRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX vsyscall=none"'                                  >> /etc/default/grub''')
os.system('''echo 'GRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX debugfs=no-mount"'                               >> /etc/default/grub''')
os.system('''echo 'GRUB_CMDLINE_LINUX="$GRUB_CMDLINE_LINUX debugfs=tsx=off"'                                >> /etc/default/grub''')

os.system('update-grub')
