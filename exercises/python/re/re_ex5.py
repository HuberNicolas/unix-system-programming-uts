#!/usr/bin/python3
import re

#Our regx to find 'words then @ words dot then au'
test_regx = r'\w+@(?:\w+\.)*\w+\.au\b'
test_regx = r'\w+@\w[\w.-]*\w\.au'
test_regx = r'\w+@(\w+\.)+au'
#We read a line of input. No need to prompt.
read_text = input()

#use match
into_data = re.match(test_regx,read_text)#YOUR CODE
if into_data :
    print("matched")
else :
    print("not matched")

