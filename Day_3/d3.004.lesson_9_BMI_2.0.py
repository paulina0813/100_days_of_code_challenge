'''
Instructions
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Equal to or over 25 but below 30 they are slightly overweight
Equal to or over 30 but below 35 they are obese
Equal to or over 35 they are clinically obese.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
BMI = weight(kg) / height^2(m^2)

Important: you do not need to round the result to the nearest whole number. It's fine to print out a floating point number for this exercise. The interpretation 
message needs to include the words from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.
'''
height = float(input("Please enter your height in meters: "))
weight = float(input("Please enter your weight in kg: "))

bmi = weight / height ** 2

if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}, you have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}, you are slightly overweight.')
elif bmi < 35:
    print(f'Your BMI is {bmi}, you are obese.')
else:
    print(f'Your BMI is {bmi}, you are clinically obese.')