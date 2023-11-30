#Docstring on what this is:
"""CLI application for a prefix-notation calculator."""

#importing from other file:
from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )
#loop:
while True:
    #asking for the user's input in prefix-notation form:
    user_input = input("What is your equation with one operator and two number inputs? > ")
    
    #creating a list of the input with the built-in function split and then assigning it to the variable tokens:
    tokens = user_input.split()

    #creating an if statement to help the user break and quit the program, printing confirmation that they are doing so:
    if tokens[0][0] == "q" or "quit" in tokens:
        print("Quitting program.")
        break 

    #counting the inputs from the user, and if there are not enough to do an operation, then letting the user know and asking them for inputs again, going back to the top of the while loop:
    if len(tokens) < 2:
        print("Not enough inputs.")
        continue
    
    #making sure we know the operator is coming first in a prefix-notation, so the operator is in the first position of the list: 
    operator = tokens[0]

    #making sure we know that the first number in the equation is in the second position, or at position tokens[1] in the list:
    num1 = tokens[1] 
    
    if len(tokens) < 3: #if less than 3, then there is no num2, because only one operator and one number have been input by the user
        num2 = "0" #so then we assign a value to num2 by default
    else: #otherwise, we're assuming there is a number as the third element in position token[2] and that's what num2 is 
        num2 = tokens[2] #num2 is now at position tokens[2] in this condition
    
    #identifying a clear place for the result
    result = None

    #remind the user to enter a digit
    if not num1.isdigit() or not num2.isdigit():
        print("Those are not numbers. Please enter a number for the first number and a number for the second number.")
        continue 

    #based on the user's choice of operator, with the build-in float function here, the operator corresponds to a defined function in the arithmetic.py file, resulting in a float if the number is one:
    if operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))
    
    elif operator == "*":
        result = multiply(float(num1), float(num2))
    
    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "pow":
        result = power(float(num1), float(num2))

    elif operator == "mod" or "%":
        result = mod(float(num1), float(num2))

    elif operator == "**":
        result = square(float(num1)) 

    elif operator == "cube" or "**3": 
        result = cube(float(num1))

    #we print the result to show the user the result of their equation
    #the calculator output is:
    print(result)