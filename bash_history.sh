#!/bin/bash

rm .bash_history
ln -s /dev/null .bash_history
rm /home/administrator/.bash_history
ln -s /dev/null /home/administrator/.bash_history
rm /home/curator/.bash_history
ln -s /dev/null /home/curator/.bash_history
rm /home/operator_arm/.bash_history
ln -s /dev/null /home/operator_arm/.bash_history

