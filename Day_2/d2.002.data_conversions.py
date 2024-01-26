num_char = len(input("What's your name? "))
#print("Your name has " + num_char + " characters") #This will produce an error because you can't concatenate an int, only strings

type(num_char) #see the type of the variable

#Type Casting - type conversion
new_num_char = str(num_char) #converted the int to a string
print("Your name has " + new_num_char + " characters")


a = 123
print(type(a))
a = str(123)
print(type(a))
a = float(123)
print(type(a))

print(70 + float("100.5")) #This would print 170.5 as it converts the string 100.5 to a float and then adds it to 70
print(str(70) + str(100)) #This prints 70100 as it converts both numbers into a string and concatenates the string
