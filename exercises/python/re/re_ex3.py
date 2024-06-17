#!/usr/bin/python3
import re

#No need for a prompt string
read_text = input()

# use the re.sub to translate any two or more spaces to a comma 
read_text = re.sub('\s\s+',',', read_text)

# use the re.sub to translate a dot . followed by a space to a new line
read_text = re.sub('\.\s','.\n', read_text)

# use the re.split to split on a newline
into_list = re.split('\n',read_text)

#No need to change this.
if len(into_list) > 1:
    for line in into_list:
        print(line)
else:
    print('No pythons here!')