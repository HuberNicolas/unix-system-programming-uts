import sys
height = int(sys.argv[2])
shape = str(sys.argv[1])

if shape == "circle":
    print("The shape is a circle")
        
elif shape == "square":
    print("The shape is a square")
    print("Area is", height**2)
elif shape == "rectangle":
    length = int(sys.argv[3])
    print("The shape is a rectangle")
    print("Area is", height*length)    
else:
    print("The entered shape is invalid")