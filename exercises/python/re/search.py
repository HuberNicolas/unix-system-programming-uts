import re
from_text = 'Anaconda'
find_regx = r'a'
into_data = re.search(find_regx,from_text)
if into_data != None :
    print ("into_data match object =",into_data)
    #<_sre.SRE_Match object; span=(2, 3), match='a'>
    print("start =",into_data.start())
    print("end =",into_data.end())
    print("span =",into_data.span())
    print("group =",into_data.group())
    print("string =",into_data.string)
