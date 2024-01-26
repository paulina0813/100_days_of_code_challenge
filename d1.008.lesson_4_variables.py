'''
Instructions
- This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable 
called b.
- Write a program that switches the values stored in the variables a and b.
- Warning . You don't need to print anything. The print statement is already in the template code. However, your program 
should work for different inputs. e.g. any value of a and b.
'''
a = input("Enter a value for a: ")
b = input("Enter a value for b: ")

c = a #we're adding an extra variable c to store the original value of a before overwriting it
a = b #after this statement, a is equal to the original value of b
b = a #after this statement, b is equal to the original value of a, which was stored in variable c

print("a: " + a)
print("b: " + b)