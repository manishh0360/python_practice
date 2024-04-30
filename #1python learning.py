print("******CALCULATOR******")

num1 = int(input("Enter the First number: "))
Operator = str(input("Enter Operators: "))
num2 = int(input("Enter the Second number: "))


#Entered_Number= int(input("Enter number from 1 to 5:  "))

if Operator == '+':
    print(num1 + num2)

elif Operator == '-':
    print(num1 - num2)

elif Operator == '*':
    print(num1 * num2)

elif Operator == '/':
    print(num1 / num2)

elif Operator == '**':
    print(num1 ** num2)
