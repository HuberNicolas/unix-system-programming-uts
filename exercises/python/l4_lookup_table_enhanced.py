#!/usr/bin/python3
import sys
import re


def verify_argv() :
    if len(sys.argv) < 2:
        print('Not enough arguments provided!')
        exit(1)
    else:
        pass
   #ADD YOUR CODE TO TEST AND EXIT IF NOT ENOUGH ARGS


def assign_prep_dict() :
    #Our reserve word list.They are bit out of order.
    word_list=["if","and","as","assert","async","break","False","None","True",
              "class","continue","return","or","elif","else","except","finally",
              "for","from","global","await","import","in","lambda","nonlocal",
              "try","while","with","is","not","pass","raise","yield","def","del"
              ]
    
    #We create a dict type called word_dict with keys from word_list 
    #and values 0
    # MODIFY TO RETURN A DICT
    d = dict.fromkeys(word_list,0)
    return d
#End def

#COMPLETE THE UPDATE FUNCTION
def update_dict(code_line_list,word_dict):
   for word in code_line_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            pass
#End def

def read_file_data(file_name_text, word_dict):

    file_data = open(file_name_text, "r")
    text_line = file_data.readline()
    while text_line :
        tidy_text = text_line.strip()
        line_list = re.split(' ',tidy_text)
        #print(line_list)
        update_dict(line_list,word_dict)
        text_line = file_data.readline()
    #End while
    file_data.close()
    
#We loop over the input arguments from 1

#Write a function to report.
def report_word_tote(word_dict):
    # print(word_dict)

    print('Result of the lookup table:')
    for k, v in word_dict.items():
        print(f'Key {k}, has {v} occurences')

#End def

#The main code.

#Test for correct input
verify_argv()

file_name = sys.argv[1]

#Create a dict type with word list
word_dict=assign_prep_dict()

#print(word_dict)

#Read each line in the file and add to dict as needed.
read_file_data(file_name,word_dict)

#Show our result.
report_word_tote(word_dict)



