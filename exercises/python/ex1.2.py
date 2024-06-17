import sys


n = len(sys.argv)-1 # minus 1 because the script name is also included
arguments = sys.argv[1:]
arguments = [int(i) for i in arguments]

if n == 0:
    print('There are no arguments')
elif n == 1:
    print(arguments[0])
elif n == 2:
    result = arguments[0]*arguments[1]
    print(result)
elif n == 3:
    result = (arguments[0]+arguments[1])**arguments[2]
    print(result)
elif n > 3:
    print('Too many arguments entered')
else:
    pass
