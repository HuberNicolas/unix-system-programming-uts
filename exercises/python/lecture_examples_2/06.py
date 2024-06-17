#!/usr/bin/env python3
# findall tester

import sys
import re

regex = input('Enter a regular expression: ')
print('Regex: ', regex)

print('Enter some lines:')
for line in sys.stdin:
    line = line.rstrip('\n')
    x = re.split(regex,line)
    print('Split parts: ', x)
