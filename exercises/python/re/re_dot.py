import re
#Examples are non overlapping serach.
from_text = 'Anaconda'
find_regx = r'n.'
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
#into_list = ['na', 'nd']