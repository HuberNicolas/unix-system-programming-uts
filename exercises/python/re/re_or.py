import re
#Examples are non overlapping serach.
from_text = 'The tut_32547_Autumn was 100 to 2000 times more exciting '
find_regx = r'\d\d\d|was' #match 3 digits or was
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
find_regx = r'2\d\d|\d\W' #2followd by two digits OR a digit and a non word. 
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
find_regx = r'\d\d|\w{4}\W|Au' #two digits or four word then none word or Au
into_list = re.findall(find_regx,from_text)
print ("into_list =", into_list)
