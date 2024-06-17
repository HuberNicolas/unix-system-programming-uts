#!/usr/bin/python3
import re

find_regx = '\d'#YOUR CODE 
line_tote=0

read_line = input()
while read_line != '':
    into_data = re.search(find_regx,read_line)#YOUR CODE
    if into_data:#YOUR CODE
        line_tote = line_tote + 1
        print (read_line)
    #End if read next line.
    read_line = input()
#End while

if line_tote == 0:
    print('No lines matched!')