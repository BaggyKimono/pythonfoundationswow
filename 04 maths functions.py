"""
title: 04mathsfunctions
author: Ally
date: 11/26/18 11:01 AM
"""

"""

1. Math!
1.1. Arithmetic operators
1.2. Operator precedence
1.3. Other operators

"""


""" ________________________________Math!_________________________________"""

"""-------------1.1. Arithmetic operators------------------"""


Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication and division.

                    Table 1. Arithmetic Operators

                    Name	              Operator

                    Addition                 +
                    Subtraction              -
                    Multiplication           *
                    Float Division           /
                    Integer Division        //
                    Negation                - \
                    Remainder                %
                    Exponent                **


# Open IDLE by typing command + spacebar, type idle and hit return.
# Python is an interpreted language, and we can use the Python Console
# to type any numbers or commands just like a calculator.

# Try typing a few numbers, and view the output.

            Python 2 treated division differently: the / symbol would default to integer division.

# Now, let’s try a few expressions with some of the arithmetic operators:


            35 + 5
            45 - 5
            8 * 5
            400 / 10
            400 // 10
            -35 + -5
            40 % 10000

# Each of these expressions should evaluate to 40 in your python shell
# (except for the negation expression, which should evaluate to -40)

        One thing to note is that when using the / operator, the result will return as a float.


!!!!------------------------------------------------------------------------------------------------------ !!!!
        In the above example, 400 / 10 evaluates to 40.0
        If you want a whole number returned, use the // double-slash operator.
!!!!------------------------------------------------------------------------------------------------------ !!!!


!!!!------------------------------------------------------------------------------------------------------ !!!!
        Just remember that whenever you see a number without a decimal point, python is
        interpreting it as an int, and when there is a number with a decimal point, it’s a float.
!!!!------------------------------------------------------------------------------------------------------!!!!



        This is important to note for now, because as we move on to learning about loops we’ll realize that
        Python is opinionated on which operator can be used in specific situations.



!!!!------------------------------------------------------------------------------------------------------!!!!
        Also, let’s talk about the remainder operator, also called modulus.
        This will return a whole number which will be the remainder of the expression.
        For example, 10 % 3 will output 1, since 1 is the remainder when you divide 10 by 3
!!!!------------------------------------------------------------------------------------------------------!!!!





"""-------------1.2. Operator precedence------------------"""

# All operators are not equal. Remember the PEMDAS rule from math class! Let’s take a look.

            # When you take our expressions from the previous example, and put them
            # into a more complex expression, we can see how operator precedence works.

    Type the following into IDLE:

            10 + 5 / 3 - 4 * 12

           # If you go through this expression in order, as 10 + 5 is 15, dividing by 3 gives us
           # 5 and subtracting 4 leaves us with 1 before dividing by 12. You may be lead to believe
           # the answer is 12 when it is in fact -36.333333333333336 (We see the float because we
           # used the single / divisor)

    When you look at an expression like this and use PEMDAS, we have to first use multiplication to
    get 4 * 12 = 48, then take the value for b and do 3/3 which is 1.0. Then add 12 + 1.0,
    and finally 13.0 - 48 which gives us -36.333333333333336

Put your knowledge to work!



Using the same operators and numbers as the previous example, what does the following expression evaluate to when you put it into IDLE?

(((10 + 5) / 3) - 4) * 12
1.3. Other operators
There are other operators in Python, and we’ll list them briefly here and go into them in more detail later on:

Relational Operators	Relational operators compare values. It either returns True or False according to the condition.
Logical operators

Logical operators perform logical and, logical or and logical not operations.

Assignment operators

Assignment operators are used to assign values to the variables.

Special operators

There are some special types of operators like identity operators is and is not. The identity operators are used to check if two values are located on the same part of the memory. Two variables that are equal does not imply that they are identical.

Membership operators

in and not in are the membership operators; used to test whether a value or variable is in a sequence.
















#examples

'''
abs()

Finds the absolute value
'''

print(90 - 120)
print(abs(90 - 120))

'''
pow()

Raises a number to a certain power
'''

print(pow(2,3))

'''
pow()

Raises a number to a certain power
'''

print(round(17.34989436516001,4))


import random


print(random.random())
