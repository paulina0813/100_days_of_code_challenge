'''
Instructions
Try this exercise to understand how tests work with inputs in Auditorium. Write some code that multiples together 
the two numbers in the input area. When you run the tests, different inputs will replace the ones in the input area 
and pass the new inputs through your code.
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("The result of the multiplication of both numbers is:", num1 * num2)

'''
Instructions pt 2
Write a program that calculates and outputs the number of characters in any name. The automated tests will try out 
lots of different names as the input. Your code should work for any name.
'''
name = input("Please enter a name: ")
print("The length of the name entered is:", len(name))