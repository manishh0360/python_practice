num = float(input("Enter number between 1 to 100: "))

if (num<36):
    print("You are Failed.")
elif(36<=num<=100):
    if(36<=num<60):
        print("You are 3rd")
    elif(60<=num<85):
        print("you are 2nd")
    else:
        print("You are 1st")
else:
    print("Invalid number")
