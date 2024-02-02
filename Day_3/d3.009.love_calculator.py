'''
Instructions
💪 This is a difficult challenge! 💪

You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
1. Take both people's names and check for the number of times the letters in the word TRUE occurs.
2. Then check for the number of times the letters in the word LOVE occurs.
3. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is *x*, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is *y*, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is *z*."

e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"

T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times

Total = 5

L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

These functions will help you:

lower() count()
'''

print("The Love Calculator is calculating the score...")
name1 = input("Enter the name of the first person: ")
name2 = input("Enter the name of the second person: ") 

total1 = 0
total2 = 0

for letter_true in 'true':
    amount1_true = name1.lower().count(letter_true)
    amount2_true = name2.lower().count(letter_true)
    total_true = amount1_true + amount2_true
    total1 += total_true 
    print(f'{letter_true.upper()} occurs {total_true} times')
print(f'Total = {total1}')

for letter_love in 'love':
    amount1_love = name1.lower().count(letter_love)
    amount2_love = name2.lower().count(letter_love)
    total_love = amount1_love + amount2_love
    total2 += total_love 
    print(f'{letter_love.upper()} occurs {total_love} times')
print(f'Total = {total2}')

#Concatenate both
love_score = int(str(total1) + str(total2))
print(f'Love Score = {love_score}')

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
    

'''
Alternative solution

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif (score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
'''