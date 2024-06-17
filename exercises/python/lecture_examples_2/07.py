#!/usr/bin/env python3
# sub tester

import sys
import re

regex = input('Enter a regular expression: ')

repl = input('Enter the replacement string: ')

print('Enter some lines:')
for line in sys.stdin:
    line = line.rstrip('\n')
    x = re.sub(regex, repl, line) # re.sub(regex, repl, line, 1) to replace only the first match
    print('Line with replacements:', x)
