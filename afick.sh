#!/bin/bash

afick -i

setfacl -dm u:administrator:rw /var/lib/afick
setfacl -m u:administrator:r /etc/afick.conf
setfacl --recursive --modify u:administrator:rw /var/lib/afick/

