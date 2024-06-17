import re
#Example no raw strings.
from_text = 'My String is c:\\nicepath\\nicefile'
print("from_text=",from_text)
find_regx = '[a-z]:\\\\[a-z]+\\\\[a-z]+'
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)