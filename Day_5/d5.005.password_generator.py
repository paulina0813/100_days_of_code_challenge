#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
rand_letters = random.choices(letters, weights = None, k = nr_letters)
rand_numbers = random.choices(numbers, weights = None, k = nr_numbers)
rand_symbols = random.choices(symbols, weights = None, k = nr_symbols)

char_letters = ''
for letter in rand_letters:
    char_letters += letter

char_nums = ''
for number in rand_numbers:
    char_nums += number

char_symbols = ''
for symbol in rand_symbols:
    char_symbols += symbol

print(f"Password: {char_letters + char_symbols +char_nums}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
rand_letters = random.choices(letters, weights = None, k = nr_letters)
rand_numbers = random.choices(numbers, weights = None, k = nr_numbers)
rand_symbols = random.choices(symbols, weights = None, k = nr_symbols)
characters = rand_letters + rand_numbers + rand_symbols
random.shuffle(characters)

password = ''
for character in characters:
    password += character

print("Password:", password)

