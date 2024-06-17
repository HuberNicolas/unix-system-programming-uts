import re
#Examples are non overlapping serach.
from_text = 'The tutorial went on and on and on and on'
find_regx = r' (on and)*' #We a space then 'on and' zero or more times.
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
find_regx = r' (on and)+' #We a space then 'on and' one or more times.
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)