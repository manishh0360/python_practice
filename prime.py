num = int(input("Enter any number: "))
count = 0
for i in range(2,num):
   if (num%i == 0):
        count += 1
if(num==1):
    print("not prime")
elif count == 0:
    print("prime")
else:
    print("not prime")