# excercise_2:Simple calculator. Conditional statements principles applied
num1 = eval(input("Enter the first number: "))
num2 = eval(input("Enter the second number: "))
operation = (input("Enter any of the operations (+,-,*,/): "))
if operation == "+":
    result = num1 + num2
    print(result)
elif operation == "-":
    result = num1 - num2
    print(result)
elif operation == "*":
    result = num1 * num2
    print(result)
elif operation == "/":
    result = num1 / num2
    print(result)
else :
    print("Invalid operation. Try again")              