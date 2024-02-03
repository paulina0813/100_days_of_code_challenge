#Import the random module
import random
#Import my module
import my_module

random_integer = random.randint(1,10) #Random integer between 1 and 10
print(random_integer)

#use my module (file d4_002_my_module)
print(my_module.pi)

#random float
random_float = random.random() #Generates a random floating number between 0 and 1 not including 1
print(random_float)

#By mulriplying, you can expand the range from 0.0000....-0.99999.... to 0.0000....-x.9999....
randomFloat = random_float * 5 #0.00000.... - 4.9999....
print(randomFloat)

love_score = random.randint(1,100)
print(f'Your love score is {love_score}')