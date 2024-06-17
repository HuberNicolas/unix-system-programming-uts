def zeromean(l):
    mean = sum(l)/len(l)
    for i in range(len(l)):
        l[i] -= mean
my_list = [12, 24, -16, 0]
print(my_list)
zeromean(my_list)
print(my_list)
