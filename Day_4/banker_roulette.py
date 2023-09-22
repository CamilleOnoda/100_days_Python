"""You are going to write a program that will select a random name from a list of names. 
The person selected will have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.

Line 8 splits the string names_string into individual names and puts them inside a List called names. 
For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name"""

import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Using .sample(). Will print a list item ['  ']
#num_to_select = 1
#rand_name = random.sample(names, 1)

num_names= len(names)
rand_name = random.randint(0, num_names - 1)
rand_choice = names[rand_name]
print(f"{rand_choice.capitalize()} is going to buy the meal today!")
