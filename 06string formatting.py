"""
title: 06string formatting
author: Ally
date: 11/26/18 1:20 PM
"""

age = 49
#print("Monty Python is " + age + " years old.")

#convert to string

print("Monty Python is " + str(age) + " years old.")

print("Monty Python is " + str(age) + " years old.")

age = 24
print("I am {0} years old".format(age))

my_age = 24
moms_age = 60
dads_age = 59
sisters_age = 35

#each of these just refers in order (called indexing)


print("""My mom is {1} years old, and my dad is 1 year younger at {2} years old.
My sister is 11 years older than me, which makes her {3} years old
and I am only {0} years old.""".format(my_age, moms_age, dads_age, sisters_age))

my_age = 24
moms_age = 60
dads_age = 59
sisters_age = 35

print(f"""My mom is {moms_age} years old, and my dad is 1 year younger at {dads_age} years old.
My sister is 11 years older than me, which makes her {sisters_age} years old
and I am only {dads_age} years old.""")

#user input
#name = input("Enter your name: ")
#print("Nice to meet you " + name + "!")



#random Salary exercise

name = input("Enter your designator:")
salary = input("Enter your worth in: $")
print(f"{name}, your current salary is ${salary}.")

import math

import random

Random = (random.randint(1,100))

raise_per = ((random.randint(1,100)) * salary)

Print(F"Your raise is %")






