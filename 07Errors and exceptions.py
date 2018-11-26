"""
title: 07Errors and exceptions
author: Ally
date: 11/26/18 2:03 PM
"""

import random

try:
    eval('x === x')
except SyntaxError:
    print("You cannot do that")


print(10 + (1 / 0))
try:
    print(10 + (1 / 0))
except ZeroDivisionError:
    print("Oops! We can't divide by zero, please choose a different number and re-evaluate.")



