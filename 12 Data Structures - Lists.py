"""
title: 13 Sets
author: Ally
date: 11/27/18 1:19 PM
"""

"""_________________Data Structures ___________________________"""

"""

It is very common to want to list numbers or strings. This is possible with data structures. 
Data structures are a specialized format for organizing and storing data. 
There are quite a few data structures that are available that will be described in the following sections.

"""

"""_________________Lists___________________________"""

"""
A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements. 
Each element or value that is inside of a list is called an item. Just as strings are defined as 
characters between quotes, lists are defined by having values between square brackets [ ].

Lists are great to use when you want to work with many related values. 
They allow you to keep data together that belongs together, condense your code, 
and perform the same methods and operations on multiple values at once."""

"""
Data Structures Introduction
1. Lists
1.1. Length
1.2. Indexing
1.3. Slicing
1.4. Modifying
1.4.1. Adding
1.4.2. Removing
1.5. List Methods
list.append()
list.extend()
list.insert()
list.count()
list.sort()
list.remove()
"""
















#Example: Creating a list of strings called dogs

dogs = ["Collie", "Labrador", "Sheltie", "Dalmatian"]

#When you print out the list, the output looks exactly like the list we created:

print(dogs)

"""________________________________________________Length_and_indexing_________________________"""

#len(), just like in a string, allows you to find the number of elements that are in a list.
# Do the following to find the length of a list:

dogs = ["Collie", "Labrador", "Sheltie", "Dalmatian"]
print(len(dogs))

#can index and call

print(dogs[1])

#t is very common to need the last item in a list. If a boss needs to fire the person with the lowest number of sales, they could find this in a sorted list that is in descending order of sales.
# To easily find the last item in a list, we can access from the list with a negative index number, by counting backwards from the end of the list, starting at -1.
# This is especially useful if we have a long list and we want to pinpoint an item towards the end of a list.

#For the same list dogs, the negative index breakdown looks like this:

print(dogs[-1])

#We can concatenate string items in a list with other strings using the + operator.

print("Charlie is a " + dogs[1])

"""________________________________________________Slicing______________________________________"""

#We can also call out a few items from the list. Let’s say we would like to just print the middle items of dogs, we can do so by creating a slice.
# With slices, we can call multiple values by creating a range of index numbers separated by a colon [start_index: stop_index]

print(dogs[1:3]) #When creating a slice, as in [1: 3], the first index number is where the slice starts (inclusive), and the second index number is where the slice ends (exclusive), which is why in our example above the items at position 1 and 2 are the items that print out.


#f we want to include either end of the list, we can get rid of the numbers in the list[x: y] syntax.
# For example, if we want to print the first 2 items in the list dogs - which would be Collie and Golden Retriever - we can do so by typing:

print(dogs[: 2]) # everything before
print(dogs[2: ]) #everything after

# Step
#One last thing that we can use with slicing is the step.
# Step is how many items to move forward after the first item is retrieved from the list.
# Before this point, we have not used the step parameter, meaning we are using the default step value of one.

#This syntax for this construction is list[x: y: z],
# with z referring to stride. Let’s make a larger list, then slice it, and give the step a value of 2:

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1: 11: 2])

#above example starts at index 1, goes up to (but not including) 11, going up by 2’s (every other item).

#OMIT - We can omit the first two parameters and use step alone with the syntax list[: : 2]

print(numbers[: : 3])

#We can print the list backwards with a negative step

print(numbers[: : -2])


"""________________________________________________Modifying__string___values_________________

We can use indexing to change items within the list, by settling an index number equal to a different value. 
This gives us greater control over lists as we are able to modify and update the items that they contain."""

#If we want to change the string value of the item at index 1 from Labrador to Golden Retriever, we can do so like:

dogs[1] = "Golden Retriever"
print(dogs)

"""________________________________________________Adding_to_lists_____________________________

Operators can be used to make modifications to lists. The + operator can be used to concatenate two or more lists together:"""

first_names = ["Noelle", "Tereza", "Raelin", "Linus"]
last_names = ["Blossom", "Chrissy", "Grover", "Devin"]
print(first_names + last_names)

#Because the + operator can concatenate, it can be used to add an item (or several) in list form to the end of another list.

first_names = first_names + ["Sally"]
print(first_names)

#+ and * operators have a compound forms += and *=. So the above example can also be written as:

first_names += ["Sally"]
print(first_names)

#If you do not place the brackets around the string you are adding, the following will happen:

first_names += "Sally"
print(first_names)

#you get ['Noelle', 'Tereza', 'Raelin', 'Linus', 'S', 'a', 'l', 'l', 'y']
#This is because Python will take the string as a list of characters, therefore adding the characters one at a time.

"""________________________________________________Removing_from_lists__________________________

.
Items can be removed from lists by using the del statement. 
This will delete the value at the index number you specify within a list."""

# From the dogs list, let’s remove the item "Sheltie". This item is located at the index position of 2.
# To remove the item, we’ll use the del statement then call the list variable and the index number of that item:

dogs = ["Collie", "Golden Retriever", "Sheltie", "Dalmatian"]
del dogs[2]
print(dogs)

# We can also specify a range with the del statement.
# Say we wanted to remove not only the item "Sheltie", but also "Dalmatian" as well.
# We can call a range in dogs with the del statement to accomplish this:

dogs = ["Collie", "Golden Retriever", "Sheltie", "Dalmatian"]
del dogs[2: ]
print(dogs)


"""________________________________________________List_Methods__________________________

Items can be removed from lists by using the del statement. 
This will delete the value at the index number you specify within a list."""

"""________________________list.append() and extend_____________________________________"""

#The method list.append(x) will add an item (x) to the end of a list.

fish = ["barracuda", "cod", "devil ray", "eel"]

# This list is comprised of 4 string items, and their index numbers range from 'barracuda' at 0 to 'eel' at index 3.
# Adding flounder to the List

fish.append('flounder')
print(fish)

# Now, we have a list of 5 string items that ends with the item we passed to the .append() method.

# It is also possible to add a list to the end of a list
# Adding a list inside a List

fish.append(['flounder', 'clown'])
print(fish)

#or to add multiple at one time ....

fish.extend(['flounder', 'down to clown'])
print(fish)

####difference is flounder clown not in brackets with extend when adding multiple values like append



"""________________________list.insert()________________________________________________"""

#The list.insert(i,x) method takes two arguments, with i being the index position you would like to add an item to, and x being the item itself.

# Our aquarium acquired another new fish, an anchovy.
# You may have noticed that so far the list fish is in alphabetical order.
# Because of this, we don’t want to just add the string 'anchovy' to the end of fish with the list.append() method.
# Instead, we’ll use list.insert() to add 'anchovy' to the beginning of this list at index position 0:

fish.insert(0, 'anchovy')
print(fish)

# In this case, we added the string item to the front of the list.
# Each of the successive items will now be at a new index number as they have all moved down.
# Therefore, 'barracuda' will be at index 1, 'cod' will be at index 2, and 'flounder' — the last item — will be at index 5.

#If, at this point, we are bringing a damselfish to the aquarium and we wanted to
# maintain alphabetical order based on the list above, we would put the item at index 3: fish.insert(3,'damselfish').


"""________________________list.count()________________________________________________"""

# list.count() method will return the number of times the value x occurs within a specified list.
# This is useful for when you want to search a large list for the frequency of an item in a list.
# Say that you have a list of employees salaries and you would like to know how many people have the same salary as you: 20000.
# You could use could to help with this situation.

salaries = [20000, 45000, 90000, 70000, 20000, 90000]
print(salaries.count(20000))

#Because the number 20000 occurs twice, the number 2 is returned.

"""________________________list.sort()_________________________________________________"""

# We can use the list.sort() method to sort the items in a list.

# Just like list.count(), list.sort() can make it more apparent how many of a certain integer value we have,
# and it can also put an unsorted list of numbers into numeric order.

# Let’s use the integer list, fish_ages to see the .sort() method in action:

fish_ages = [1,2,4,3,2,1,1,2]
fish_ages.sort()
print(fish_ages)

