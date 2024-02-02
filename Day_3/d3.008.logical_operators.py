'''
and - both conditions need to be True for it to be True
or - only one codition needs to be True for it to be True.
not - it has to be any other value to be True
'''

'''
Example - Wroking at a theme park:
- They ahve to be at least 120cm to sell them a ticket
- There's 4 prices:
    - 5 dollars if they're under 12
    - 7 dollars if they're between 12 and 18
    - 12 dollars if they're over 18
    - It's free of they're between 45 and 55 since they fit the midlife crisis range
- If they want to add a photo package, they need to pay an aadditional 3 dollars
'''
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age in years? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18: #Since the first condition already catches everyone under 12, there's no need to add that condition here
        bill = 7
        print("Youth tickets are $7")
    elif age >= 45 and age <= 55:
        bill = 0
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12")
    
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == 'Y':
        bill += 3 #This is the same as writing bill = bill + 3
    print(f"Your final bill is {bill}")
        
else:
    print("Sorry, you have to grow taller before you can ride.")