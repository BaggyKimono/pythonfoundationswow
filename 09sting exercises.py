"""
title: 09sting exercises
author: Ally
date: 11/27/18 8:45 AM
"""

import random
import math

'''
Remove Case and Punctuation

 Create a program that has the user enter a string of any length. 
 Change the case of every letter to lower case and remove all of the occurrences of symbols and spaces.
 
 >>> Enter a phrase: Madam, I'm Adam
madamimadam
'''

name = input("Enter a phrase: ")
Answer= print("Miss I am " + name + "!")

string_1 = f"""Miss I am  + {name} + !"""
print(string_1[5:10]) #print only string #5-#10


this_thingy="this is a sentence for he splicing"
print(this_thingy[:-2])  #start begining of string and print until last 2 letters
print(this_thingy[-2:])  #start neg 2 (end of string) an print the rest



