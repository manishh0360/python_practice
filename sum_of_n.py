number = int(input("Enter number: "))
sum=0
for i in range(1,number+1):
    if (i%2==1):
        
        sum += i
       
print(sum)