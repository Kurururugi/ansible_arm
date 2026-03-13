#!/bin/bash

if [ -f .bash_history ]; then
    rm .bash_history
fi
if [ ! -L .bash_history ]; then
    ln -s /dev/null .bash_history
fi

if [ -f /home/administrator/.bash_history ]; then
    rm /home/administrator/.bash_history
fi
if [ ! -L /home/administrator/.bash_history ]; then
    ln -s /dev/null /home/administrator/.bash_history
fi

if [ -f /home/curator/.bash_history ]; then
    rm /home/curator/.bash_history
fi
if [ ! -L /home/curator/.bash_history ]; then
    ln -s /dev/null /home/curator/.bash_history
fi

if [ -f /home/operator_arm/.bash_history ]; then
    rm /home/operator_arm/.bash_history
fi
if [ ! -L /home/operator_arm/.bash_history ]; then
    ln -s /dev/null /home/operator_arm/.bash_history
fi

