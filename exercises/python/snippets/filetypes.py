var = None
my_list = [7, 11.2, 'some text', var]
my_list.append('new_element')
print(my_list)
print(my_list[-1]) # 'new_elemeet'
print(my_list[1:5]) # 11.2, 'some text', var, 'new_element'
print(my_list[1:5:2]) # 11.2, 'var'
print(my_list[3:]) # var, 'new_element'
print(my_list[:3]) # 7, 11.2, 'some text',
print(range(10))
for i in range(9):
    print(i) # 0 - 9
