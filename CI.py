Principle=int(input("Enter principle amount: "))
P=Principle
Rate=int(input("Enter rate: "))
R=Rate
Time=int(input("Enter time: "))
T=Time
C=int((P * (1 + R/100)**T) - P)
print(C)