#!/usr/bin/python3

import os

if not os.path.isfile('/etc/sysctl.d/98-fstec.conf'):
    os.system('touch /etc/sysctl.d/98-fstec.conf')

os.system('echo "kernel.kptr_restrict=2" > /etc/sysctl.d/98-fstec.conf')
os.system('echo "kernel.dmesg_restrict = 1" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "net.core.bpf_jit_harden = 2" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "kernel.perf_event_paranoid = 3" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "kernel.kexec_load_disabled = 1" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "kernel.unprivileged_bpf_disabled = 1" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "vm.unprivileged_userfaultfd = 0" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "dev.tty.ldisc_autoload = 0" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "vm.mmap_min_addr = 4096" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "kernel.randomize_va_space = 2" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "kernel.yama.ptrace_scope=3" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "fs.protected_symlinks = 1" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "fs.protected_hardlinks = 1" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "fs.protected_fifos = 2" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "fs.protected_regular = 2" >> /etc/sysctl.d/98-fstec.conf')
os.system('echo "fs.suid_dumpable = 0" >> /etc/sysctl.d/98-fstec.conf')

if not os.path.isfile('/lib/sysctl.d/99-protect-links.conf.bak'):
    os.system('cp /lib/sysctl.d/99-protect-links.conf /lib/sysctl.d/99-protect-links.conf.bak')
with open('/lib/sysctl.d/99-protect-links.conf', 'r') as f:
    lines = f.readlines()
with open("/lib/sysctl.d/99-protect-links.conf", "w") as f:
    for line in lines:
        if 'fs.protected_fifos' in line.strip():
            line = 'fs.protected_fifos = 2\n'
            f.write(line)
        else:
            f.write(line)
