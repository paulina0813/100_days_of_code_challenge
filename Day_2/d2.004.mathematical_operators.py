'''
004. Mathematical Operators
'''
3 + 5 #sum
7 - 4  #subtraction
3 * 2 #multiplication
6 / 3 #division
2 ** 2 #raise to a power. It's an exponent

'''
If there is more than one mathematical operation, they have to follow an order as stated by PEMDAS
- Parenthesis
- Exponents
- Multiplication
- Division
- Addition
- Subtraction 
()
**
* / #equally important. The one that's most to the left will be done first
+ - #equally important. The one that's most to the left will be done first
'''
print(3 * 3 + 3 / 3 - 3) #It will multiply 3*3, then divide 3/3, then add the result of the multiplication to the result of the subtraction, and then subtract the final 3
print(3 * (3 + 3) / 3 - 3) #This will add 3+3, then multiply that result *3, then divide by /3, and then subtract 3