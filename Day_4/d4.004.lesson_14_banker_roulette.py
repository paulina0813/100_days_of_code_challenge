'''
Instructions

You are going to write a program that will select a random name from a list of names. The person selected will have to pay for everybody's food bill.
Important: You are not allowed to use the choice() function.
Line 1 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as names followed by comma then space. e.g. name, name, name
Note: Don't worry about getting hold of the input(), we've done the work behind the scenes to import everything.
HINT: Assume that names looks like this: input: x, y, z, names = ["x", "y", "z"]

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!

Hints
You might need the help of the len() function. https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list
Remember that Lists start at index 0!
'''
import random

names_string = input("Please enter some names separated by a comma: ")

#This code converts the input into an array seperating
# each name in the input by a comma and space.
names = names_string.split(", ")
length = len(names)

#Generate a random number to have a random index
index = random.randint(0,length - 1) #You have to subtract 1 because the index starts at 0, not 1

#Select a random person
print(f'{names[index]} is going to buy the meal today!')