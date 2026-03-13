#!/bin/bash

if [ -f /etc/xdg/autostart/hplip-systray.desktop ]; then
    rm /etc/xdg/autostart/hplip-systray.desktop
fi
if [ -f /etc/xdg/autostart/baloo_file.desktop ]; then
    rm /etc/xdg/autostart/baloo_file.desktop
fi
if [ -f /etc/xdg/autostart/kscreen.desktop ]; then
    rm /etc/xdg/autostart/kscreen.desktop
fi

