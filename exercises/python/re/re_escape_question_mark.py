import re
#Examples are non overlapping serach.
from_text = 'Does Angela own an Anaconda? Does she own a Python ?'
find_regx = r'\?' #We escape the meta character.
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)