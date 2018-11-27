"""
title: 09Concatenation
author: Ally
date: 11/26/18 3:02 PM
"""

#credentials generator


input = ("What is your name?")
Input = 



print("===Credentials Generator===")

'''
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
birth_city = input("Enter Birth City: ")
alma_mater = input("Enter Alma Mater University: ")
relatives_name = input("Enter a Relative's Name: ")
friends_name = input("Enter a Friend's Name: ")



Their employee id is generated with the following concatenated:
the first three letters of your first name
the last two letters of your last name


employee_id = first_name[:3] + last_name[-2:]


Their user name is generated with the following concatenated:
the first two letters of the city you were born in
the last three letters of the university they graduated from


user_name = birth_city[:2] + alma_mater[-3:]


Their password will be more randomly generated with the following concatenated:
starting at a random location to the end of your relative’s name.
starting at the beginning of your friend’s name to a random location of the string.
rnd_relative = random.randint(0, len(relatives_name)-1)
rnd_friend = random.randint(1, len(friends_name))
password = relatives_name[rnd_relative:] + friends_name[:rnd_friend]
password = password[0].upper() + password[1:].lower()

#
print("Employee ID:", employee_id)
print("User Name:", user_name)
print("Password:", password)
'''

print("\n===Remove Case and Punctuation===")
phrase = input("Enter a phrase: ")

phrase = phrase.lower().replace(" ", "").replace(".", "").replace(",", "").replace("'", "").replace('"', "")
print(phrase)

print("\n===Palindrome Checker===")
print(phrase[::-1] == phrase)



Collapse 

Message Input

Message #python-foundation-atl

Thread
#merch-it

