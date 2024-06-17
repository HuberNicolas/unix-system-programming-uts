import re
#Examples are non overlapping serach.
from_text = 'The tut_32547_Autumn was 100 to 2000 times more exciting '
find_regx = r'\d{2}' #any two digits
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
find_regx = r'\d{4,4}' #any four digits 
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
find_regx = r'\d\d\d\d' #any four digits 
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
