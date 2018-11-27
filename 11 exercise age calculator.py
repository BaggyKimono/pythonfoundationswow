"""
title: 11 exercise age calculator
author: Ally
date: 11/27/18 9:49 AM
"""

#creates dictionary of all keyword arguements that were passed in
#*matters what its called (args or kwargs) doesn't matter

#print keywords - i named my argument in a function

#key are L, W, height

#parameters - is when you actually define this function =

#arguement when i call the function = area()

# * before pulls all arguements not assigned to a value


#create a login - required vs optional information - required parameters are sent, but option one's are not
'''
def area(*args, **kwargs):
    print(kwargs)
    print(args)

height = 20
area(height, l=10, w=40)

# to get single value
def area(*args, **kwargs):
    print(kwargs)
    print(kwargs["l"])
    print(args)

height = 20
area(height, l=10, w=40)

#way to see if funation contains a key
def areas(**keywordarg):
    if (keywordsarg['uname']):
        print(keywordarg['uname'])

'''

Def age_calculator()