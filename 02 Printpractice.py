"""
title: Printpractice
author: Ally
date: 11/26/18 10:36 AM
"""

print("hello world")

#new line

print("hello world\nhell is other people")

#end a print statement with a thingy

print("newline", end = "-")

#tabbed characters


print("Testing, testing\t1\t2\t3...")

print("Testing, testing\n\t1\n\t\t2\n\t\t\t3...")

#Comments

'''
This is an example of a multi-line
comment in python. If you have a lot
to say about how the program runs
you can put a block of comments like so!
'''

#a function

def somefunc():
    """
    This function does xyz
    :return:
    """

#a typical way to describe a detail of a function

def greeting(name, year):
    """
    Greet the user with a friendly hello and inform them of the year
    :param name: a string that stores the users name
    :param year: an integer that stores the current year
    :return: the concatenated string
    """
    return "Hello from the other side," + name + "! It is " + str(year)
