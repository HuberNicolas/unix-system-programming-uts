#!/usr/bin/python3
import re

#We prompt the user
read_text = input("Enter some text\n")

#Write some regex in the variable test_regx to produce our desired match.
#test_regx = "(?i)python"
test_regx = "python"

#add options to findall if necessary if not fix the code.
find_list = re.findall(test_regx,read_text, flags=re.IGNORECASE)

if len(find_list) != 0:
    print(find_list)
else:
    print('No pythons here!')