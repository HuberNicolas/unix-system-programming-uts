#!/usr/bin/env python3
# re tester

import sys
import re

regex = input('Enter a regular expression: ')
print('Regex: ', regex)

print('Enter some lines:')
for line in sys.stdin:
    line = line.rstrip('\n')
    x = re.search(regex, line)
    if  x:
        print('Line: ', line)
        print('Matched part: ', x.group())
