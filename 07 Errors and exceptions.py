"""
title: 07Errors and exceptions
author: Ally
date: 11/26/18 2:03 PM
"""

import random
print(4 + spam * 3)

try:
  print(4 + spam * 3)
except NameError as error:
  print('You have encountered a NameError because', error)


print(10 + (1 / 0))
try:
    print(10 + (1 / 0))
except ZeroDivisionError:
    print("Oops! We can't divide by zero, please choose a different number and re-evaluate.")



