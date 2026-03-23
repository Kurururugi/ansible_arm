#!/bin/bash

disk_state=`megacli -LDInfo -LALL -aALL | grep State`
if [ "$disk_state" == 'State               : Optimal' ]
then
        echo 1 > /usr/local/Project/raid_state
else
        echo 0 > /usr/local/Project/raid_state
fi

time_state=`chronyc tracking | grep Leap`

if [ -z "$time_state" ]
then
	time_state="err"
fi

if [ "$time_state" == 'Leap status     : Normal' ]
then
        echo 1 > /usr/local/Project/time_state
else
        echo 0 > /usr/local/Project/time_state
fi
exit 0
