#!/bin/bash

touch /etc/X11/xorg.conf
echo 'Section "ServerFlags"' > /etc/X11/xorg.conf
echo '    Option "DontVTSwitch" "true"' >> /etc/X11/xorg.conf
echo 'EndSection' >> /etc/X11/xorg.conf


