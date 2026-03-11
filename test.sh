#!/bin/bash

sed -i -e 's/kernel.yama.ptrace_scope = 3/kernel.yama.ptrace_scope = 1/' /usr/local/Project/test.txt
