print("Welcome to my computer quiz!")
playing = input("Do  you  want  to  play? ")

if playing != "yes":
    quit()
    
print("Okay lets play :)")

print ("Question: What does CPU stands for? ")
Answer = input ().lower
if Answer == "central processing unit":
    print ("correct!")
else :
    print ("incorrect!")

print ("Question: What does GPU stands for? ")
Answer = input ().lower
if Answer == "graphics processing unit":
    print ("correct!")
else :
    print ("incorrect!")

print ("Question: What does RAM stands for? ")
Answer = input ().lower
if Answer == "random access memory":
    print ("correct!")
else :
    print ("incorrect!")

print ("Question: What does ROM stands for? ")
Answer = input ().lower
if Answer == "read only memory":
    print ("correct!")
else :
    print ("incorrect!")

print ("Question: What does PSU stands for? ")
Answer = input ().lowerp
if Answer == "power supply unit":
    print ("correct!")
else :
    print ("incorrect!")