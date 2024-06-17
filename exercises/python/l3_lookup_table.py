#!/usr/bin/python3
import sys

#Our reserved word list it's a bit out of order.
word_list=["if","and","as","assert","async","break","False","None","True",
           "class","continue","return","or","elif","else","except","finally",
           "for","from","global","await","import","in","lambda","nonlocal",
           "try","while","with","is","not","pass","raise","yield","def","del"
           ]
#We create a dict type called word_dict with keys from word_list and values 0
word_dict = {word:0 for word in word_list}
#Use print(word_dict) to see it.
#print(word_dict)

#Loop over the input arguments from 1
#If the a imput word is in the dict 
#Increment its value
i=1
while i < len(sys.argv) :
    keyword = sys.argv[i]
    if keyword in word_dict.keys():
        word_dict[keyword] += 1
    i+=1
#End while



#We loop over the sorted (!) list. Show only the 
#keys and values with values greater than 0
sorted_word_dict = dict(sorted(word_dict.items())) 
for key, value in sorted_word_dict.items():  
    if value > 0:
        print(f'{key} {value}')
    