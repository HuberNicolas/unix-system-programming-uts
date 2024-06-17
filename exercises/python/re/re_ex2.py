#!/usr/bin/python3
import re

#We prompt the user don't change this.
read_text = input("Enter some text\n")
find_regx = "python"#what word are we looking for?

into_data = re.search(find_regx, read_text)

if into_data is None:
    print("No pythons here!")#what happens if we dont find anything?)
else:
    print(into_data.start())#what kind of output do we want?)