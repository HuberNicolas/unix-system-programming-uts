import re
#Examples are non overlapping serach.
from_text = 'Anaconda and Python are snakes'
find_regx = r'^A' #We match starts with an A.
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
from_text = 'Python and Anaconda are snakes'
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
find_regx = r'.$' #We match any single last character.
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)