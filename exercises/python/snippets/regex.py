import sys
import re
regex = input('Enter a regular expression: ')
print('Regex: ', regex)
print('Enter some lines:')
for line in sys.stdin:
    line = line.rstrip('\n')
    match = re.search(regex,line) # x 
if match:
    print('Line :', line)
    #print('Span: ', match.span())
    #print('String: ', match.string)
    print('Matched part: ', match.group())
