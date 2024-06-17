import re
from_text = 'Angela owns an Amazonian Anaconda'
regx_text = r' '
into_list = re.split(regx_text,from_text)
print (into_list)
#['Angela', 'owns', 'an', 'Amazonian', 'Anaconda']