#!/bin/bash

disk_state=`megacli -LDInfo -LALL -aALL | grep State`
if disk_state=='State               : Optimal'
then
   echo 1 > /usr/local/Project/raid_state
else
   echo 0 > /usr/local/Project/raid_state
fi

exit 0
