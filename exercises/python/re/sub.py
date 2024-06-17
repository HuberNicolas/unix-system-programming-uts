import re
read_from_text = 'Angela owns an Amazonian Anaconda'
test_when_regx = r'Anaconda'
swap_with_text = 'Python'
made_into_text = re.sub(test_when_regx,swap_with_text,read_from_text)
print ("made_into_text =",made_into_text)

#Angela owns an Amazonian Python