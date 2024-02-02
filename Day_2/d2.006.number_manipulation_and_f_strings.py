'''
006. Number Manipulation
'''
#Rounding numbers
print(int(8 / 3)) #Gets rid of the entire decimal part and just prints out the integer. ince the result is 2.6666665, it will print 2
print(round(8 / 3)) #Rounds the number up to the closest integer. Since the result is 2.6666665, it will round to 3
print(round(8 / 3, 2)) #Rounds the number to the specified number of decimals. Since the result is 2.6666665, and we put a 2 after, it will print 2.67
print(round(2.666666665, 3)) #Rounds the number to the specified number of decimals. Since we put a 2 after, it will print 2.667

#Floor division - The result is an int
print(8 // 3) #This converts it into an integer right away and gets rid of all the decimals without the need to type cast. This will print 2

#Multiple operations
result = 4 / 2 #Divides 4 / 2 and stores it in the variable result
result /= 2 #Divides what was stored in result (2) by 2
print(result) #Prints the result of  4 / 2 / 2


#f-strings
score = 0
height = 1.8
isWinning = True
print("Your score is " + str(score)) #With this type of print, you have to type cast to string before printing

print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}") #It allows you to print everything regardless of data type
