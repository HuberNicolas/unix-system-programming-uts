import re
from_text = 'Example of case insensitive match'
find_regx = r'example'
into_data = re.match(find_regx,from_text,re.IGNORECASE)
if into_data != None :
    print ("into_data match object =",into_data)
    #<_sre.SRE_Match object; span=(2, 3), match='a'>
    print("start =",into_data.start())
    print("end =",into_data.end())
    print("span =",into_data.span())
    print("group =",into_data.group())
    print("string =",into_data.string)
