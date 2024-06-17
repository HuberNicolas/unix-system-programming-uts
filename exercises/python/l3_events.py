#!/usr/bin/python3
import sys

#Add event tuples to this.
event_list =[]

line_text = ''
while line_text != None :
    name_text=input('Enter event name or q to quit: ')
    if name_text == 'q':
        break #End the loop early.
    #End if 
    dist_numb=float(input('Enter distance d: '))
    time_numb=float(input('Enter time t: '))
   

    if time_numb**2 > dist_numb**2:
        # create tuple
        tu =(name_text, dist_numb, time_numb)
        event_list.append(tu)
       
#End while

print("Time-like events:")
print(event_list)