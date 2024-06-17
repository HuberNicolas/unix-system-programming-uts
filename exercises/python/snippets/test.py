import sys
import re

user_input = str(input("Please enter you student id: "))
pattern = r'(?i)Python'
findall = re.findall(pattern, user_input)

print(findall)

print(sys.argv[0], sys.argv[1])

