"""
title: 08boolean
author: Ally
date: 11/26/18 2:20 PM
"""


"""
Boolean Introduction
A boolean is a data type that can be either true or false.

It is raining - True

5 is greater than 8 - False

Orange Method is the best - True

Booleans are used to make comparisons and to control the flow of a program. 
Named for George Boole, the word Boolean always begins with a capitalized B. 
The values True and False will also always be with a capital T and F respectively, as they are special values in Python.

You can create variables and set them to either True or False
"""
is_tired = False
is_available = True

# You can also cast a boolean values to an integer. 0 represents False and 1 represents True.

print(int(True))
print(int(False))

#          Output:1 AND 0






"""_________________Comparison Operators ___________________________"""

In programming, comparison operators are used to compare values and evaluate done to a single Boolean value of either True or False.

The table below shows Boolean comparison operators.

Operator	What it means
  ==          Equal to
  !=          Not Equal to
  <           Less than
  >           Greater than
  < =         Less than or equal to
  >=          Greater than or equal to

#   To understand how these operators work, let’s assign two integers to two variables in a Python program:


x = 5
y = 8

# We know that in this example, since x has the value of 5, it is less than y which has the value 8.

# Using those two variables, we will show the above operators being used.

x = 5
y = 8

print("x == y:", x == y)
print("x != y:", x != y)
print("x < y:", x < y)
print("x > y:", x > y)
print("x <= y:", x <= y)
print("x >= y:", x >= y)

            Output:

                    x == y: False
                    x != y: True
                    x < y: True
                    x > y: False
                    x <= y: True
                    x >= y: False



#  Following mathematical logic, in each of the expressions above, Python has evaluated:

        Is 5 (x) equal to 8 (y)? False

        Is 5 not equal to 8? True

        Is 5 less than 8? True

        Is 5 greater than 8? False

        Is 5 less than or equal to 8? True

        Is 5 not less than or equal to 8? False

# All of these comparators can work with floating point values and strings as well.
# Strings are case-sensitive unless you use an additional string method.


name1 = "Sally"
name2 = "sally"
print("Sally == sally: ", name1 == name2)

        Output: Sally == sally: False

________________________________________________________________________________________________
Note: There is a difference between the two operators = and ==.

x = y sets (changes) the value of x to be equal to y

x == y asks if the value of x equals the value of y. No values are changed.

________________________________________________________________________________________________


"""_________________Logical Operators ___________________________"""


There are three logical operators that are used to compare values.

These operators are and, or, and not.


Operator	   What it means	             What it looks like
  and        True if both are true               x and y
  or         True if at least one is true        x or y
  not        True only if false                  not x





                and example

# To join the local basketball team, you must be at least 4 foot tall and at least 16 years old.
# Here are all the ways you would not be able to join the team:

    If you were at least 4 foot tall, but not at least 16 years old

    If you were less than 4 foot and at least 16 years old

    If you were less than 4 foot and less than 16 years old

# The only way you would be able to join the team would be if you were both taller than 4 foot and at least 16 years old.





                or example

# Say they were not able to find enough people who fulfilled both requirements for the basketball team,
# so they made it to where you just have to meet one or more of the requirements.
# Now to join the local basketball team, you must be at least 4 foot tall or at least 16 years old.
# Here are now all of the ways you can join the team:

    If you were at least 4 foot tall, but not at least 16 years old

    If you were less than 4 foot and at least 16 years old

    If you were at least 4 foot tall, and at least 16 years old

# The only way you would be able to not join the team if you were neither taller than 4 foot or at least 16 years old.




                Example Uses of and, or and not


print((9 > 7) and (2 < 4))  # Both expressions are True
print((8 == 8) or (6 != 6)) # One expression is True
print(not(3 < = 1))         # The expression is True

                Output:

                True
                True
                True

#  In the first case:

print((9 > 7) and (2 < 4))

        # Both 9 > 7 and 2 < 4 needed to evaluate to True since the and operator was being used.

In the second case:


print((8 == 8) or (6 != 6))

        #  Since 8 == 8 evaluated to True, it did not make a difference that 6 != 6 evaluates to
        #  False because the or operator was used. If we had used the and operator, this would evaluate to False.

In the third case:


print(not(3 < = 1))
         #  The not operator negates the False value that 3 < = 1 returns.




"""___________________________________________________________________________________________"""
"""___________________________________________________________________________________________"""
"""________________________Boolean Exercise___________________________________________________"""

print(True and True)
print(False and True)
print(1 == 1 and 2 == 1)
print("test" == "test")
print(1 == 1 or 2 != 1)
print(True and 1 == 1)
print(False and 0 != 0)
print(True or 1 == 1)
print(not (True and False)
print(not (1 == 1 and 0 != 1)
print(not (10 == 1 or 1000 == 1000)
print(not (1 != 1 or 3 == 4)
print(not ("testing" == "testing" and "Ronny" == "Gool Guy")
print(1 == 1 and not ("testing" == 1 or 1 == 0)
print("chunky" == "bacon" and not (3 == 4 or 3 == 3)
print(3 == 3 and not ("testing" == "testing" or "Python" == "Fun")
