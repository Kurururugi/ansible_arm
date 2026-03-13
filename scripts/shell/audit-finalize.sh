#!/bin/bash

if [ ! -f /etc/audit/rules.d/99-finalize.rules ]; then
    touch /etc/audit/rules.d/99-finalize.rules
fi

echo '-e 2' > /etc/audit/rules.d/99-finalize.rules
