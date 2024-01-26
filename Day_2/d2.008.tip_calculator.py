'''
If the bill was $150.00, split between 5 people, with 12% tip
- Each person should pay (150.00 / 5) * 1.12 = 33.6
- Round the result to 2 decimal places = $33.60
'''
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
percentage_tip  = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

amount_per_person = float(total_bill) / int(people) * (1 + int(percentage_tip) / 100)
amount_per_person = "{:.2f}".format(amount_per_person) #Ensure that there's always 2 decimal places even if the second one is 0
print(f"Each person should pay: ${amount_per_person}")