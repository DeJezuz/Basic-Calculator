#Basic Calculator Program - Power Learn Project
#Author: Gervasio

# Ask for user input
num1 = float (input("nter the first numbur: ")) 
num2 = float (input("nter the second numbur: "))
operation = input("choose operation (+, -, *, /): ") 

#Perform calculation
if operation == "+":
    result = num1 + num2
elif operation == "-"
    result = num1 - num2
elif operation == "*"    
    result = num1 * num2
elif operation == "/"
    if num2 != 0
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else: 
    result = "Invalid operation"  

# Show result
print(f"{num1} {operation} {num2} = {result}")