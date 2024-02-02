'''
Example - Wroking at a theme park:
- They ahve to be at least 120cm to sell them a ticket
- There's 3 prices:
    - 5 dollars if they're under 12
    - 7 dollars if they're between 12 and 18
    - 12 dollars if they're over 18
'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age in years? "))
    if age < 12:
        print("The price of the ticket is $5")
    elif age <= 18: #Since the first condition already catches everyone under 12, there's no need to add that condition here
        print("The price of the ticket is $7")
    else:
        print("The price of the ticket is $12")
else:
    print("Sorry, you have to grow taller before you can ride.")