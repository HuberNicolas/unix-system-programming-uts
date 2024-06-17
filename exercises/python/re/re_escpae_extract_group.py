import re
#Example using raw strings.
from_text = r'bits=8, bytes=107 and pieces=900 '
print("from_text=",from_text)
find_regx = r'.*bits=(\d+).*bytes=(\d+).*pieces=(\d+).*'
into_data = re.search(find_regx,from_text)
print(into_data)
if into_data :
    print("all groups=",into_data.groups())
    print("group 0   =",into_data.group(0))
    print("group 1   =",into_data.group(1))
    print("group 2   =",into_data.group(2))
    print("group 2   =",into_data.group(3))