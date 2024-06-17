import re
#Examples are non overlapping serach.
from_text = 'The tut_32547_Autumn was 100 to 2000 times more exciting '
find_regx = r'[a1b7]' #Non word zero or more words Non Word'
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
find_regx = r'[^a-z\d ]' #Not a lower case letter or a digit or a space
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)