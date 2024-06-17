#!/usr/bin/env python3
# example

import sys
import re

regex = 'TASK \[.*\]'
#print(regex)

for line in sys.stdin:
    line = line.rstrip('\n')
    x = re.search(regex, line)
    if  x:
        print(x.group())
