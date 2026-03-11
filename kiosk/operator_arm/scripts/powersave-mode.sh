#!/bin/bash

configdir="/home/$USER/.config"
config=$configdir/powermanagementprofilesrc

function createconfig {
    touch $config

    cat >> $config << EOF
[AC][DPMSControl]
idleTime=0

[AC][DimDisplay]
idleTime=0

[Battery][DPMSControl]
idleTime=0

[Battery][DimDisplay]
idleTime=0

[Battery][SuspendToRam]
idleTime=0

[LowBattery][DPMSControl]
idleTime=0

[LowBattery][DimDisplay]
idleTime=0

[LowBattery][SuspendToRam]
idleTime=0

EOF
}

mkdir -p "/home/$USER/.config"

if [ ! -e $config ]; then
    mkdir -p $configdir
    createconfig
fi

if grep -q "PowerSaveMode=true" $FLY_KIOSK_CONFIG_DIR/fly-kiosk.conf; then
    sed -i "s/idleTime.*/idleTime=600/g" $config
else
    sed -i "s/idleTime.*/idleTime=0/g" $config
fi

sed -i "s/;idleTime/idleTime/g" $config
