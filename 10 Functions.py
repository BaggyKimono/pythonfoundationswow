"""
title: 10 Functions
author: Ally
date: 11/27/18 9:27 AM
"""

'''
Functions are important because they allow us to divide code into useful blocks. 
We can create order and organization, make it more readable, and reuse it to prevent repetitiveness.

Function syntax in Python begins with the keyword def followed by the function name, parenthesis, and a colon. 
On the second line, we need to indent appropriately or else Python will not run the function and it will error.

Copy and paste the following function into PyCharm and run it:
'''



def subtract_total():
    total = 10000
    my_share = 20000
    print(my_share - total)

#because print is inside function
#function must have indent as long as it is indented it is part of the function
# a function isn't a function is it doesn't return

subtract_total()

#have function = something and print that

sub_total = subtract_total
print(sub_total())

def subtract_total (number1,number2):
    return number2 -number1

subtotal = subtract_total(1000,2000)


#what is happening


'''A parameter is placed within the parenthesis of a function. 
Parameters are declared when the function is defined as placeholders for actual objects that will be passed when the function will be called.
In Python you do not declare the type of a parameter. '''

#Code along: Write a function called hello(), and put the parameter name within the parenthesis.

def hello(name):

#We want this function to print out Hello your-name!, so we need to concatenate the string "Hello" with your name (also a string).
# So we’ll take the parameter name and use it as a variable within the print() function.

#def hello(name):
    print("Hello " + name)
#hello()

#If we run this, Python will throw a Type Error saying that hello() takes exactly 1 argument.
# When we called the function on the last line, we didn’t give hello() any arguments!

#Let’s make name our own name. To do this, we need to pass a unique argument when we actually call the function.
def hello(name):
    print("Hello " + name)
hello("Emily")

#Output: Hello Emily

#The name within the parenthesis when we define a function is called a parameter.
# When we pass data into the parenthesis while calling a function, it’s called an argument.

#For example, the function defined below utilizes a conditional statement
# to check if the input for the name variable contains a vowel, then uses a for loop to iterate over the letters in the word string.

def has_vowel(word):
    # has vowel is the name of the function
    # word is the parameter
    # Check whether name has a vowel
    #intersection is pulling the set and comparing it to whatever i feed into the function below it
    # uses parameter word, checking only for lower case vowels in whatever i feed into the function
    if set('aeiou').intersection(word.lower()):
        print(word, 'contains a vowel.')
    else:
        print(word, 'does not contain a vowel.')

    #conditional statement is added in to tell the function what to show user if the word contains a vowel or not

has_vowel("supercalifragilisticexpialidocious")
has_vowel("why")
has_vowel("hey")
has_vowel("lazy dog jumped over the tree")


"""_________________Keyword Arguments  ___________________________

In addition to calling parameters in order, you can use keyword arguments in a function call, 
in which the caller identifies the arguments by the parameter name.


When you use keyword arguments, you can use parameters out of order because the Python 
interpreter will use the keywords provided to match the values to the parameters.

Let’s create a function that will show us profile information for a user. We’ll pass parameters
to it in the form of username (intended as a string), and followers (intended as an integer).  """

 def profile_info(username, followers):
    print("Username: " + username)
    print("Followers: " + str(followers))



    