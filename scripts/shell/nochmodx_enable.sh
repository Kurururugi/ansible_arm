#!/bin/bash

systemctl --now disable avahi-daemon
systemctl --now disable vsftp
systemctl --now disable bluetooth
systemctl --now disable iscsi
systemctl --now disable iscsid

astra-sudo-control enable
astra-console-lock enable
astra-macros-lock enable
astra-ptrace-lock enable
astra-shutdown-lock enable
astra-mount-lock enable
astra-bash-lock enable
astra-interpreters-lock enable
astra-noautonet-control enable
astra-nochmodx-lock enable
