import re
from_text = 'Anaconda'
find_regx = r'a'
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)