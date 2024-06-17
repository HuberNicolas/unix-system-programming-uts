import sys
import re

student_id = str(input("Please enter you student id: "))
pattern = r'[0-9]{2}\-[0-9]{3}\-[0-9]{3}'
findall = re.findall(pattern, student_id)

print(findall)