import re
#Examples are non overlapping serach.
from_text = 'The tut_32547_Autumn was 100 to 2000 times more exciting '
find_regx = r'\W\w*\W' #Non word zero or more words Non Word'
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
find_regx = r'\D\d+\D' #Non digit one or more digits Non digit.
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
find_regx = r'\d\d\d\d' #Four digits
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
