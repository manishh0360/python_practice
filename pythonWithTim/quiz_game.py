print("Welcome to my computer quiz!")
playing = input("Do  you  want  to  play? ")

if playing.lower() != "yes":
    quit()
    
print("Okay lets play :)")
score = 0

print ("Question: What does CPU stands for? ")
Answer = input ().lower()
if Answer == "central processing unit":
    print ("correct!")
    score +=1
else :    
    print ("incorrect!")

print ("Question: What does GPU stands for? ")
Answer = input ().lower()
if Answer == "graphics processing unit":
    print ("correct!")
    score +=1
else :
    print ("incorrect!")

print ("Question: What does RAM stands for? ")
Answer = input ().lower()
if Answer == "random access memory":
    print ("correct!")
    score +=1
else :
    print ("incorrect!")

print ("Question: What does ROM stands for? ")
Answer = input ().lower()
if Answer == "read only memory":
    print ("correct!")
    score +=1
else :
    print ("incorrect!")

print ("Question: What does PSU stands for? ")
Answer = input ().lower()
if Answer == "power supply unit":
    print ("correct!")
    score +=1
else :
    print ("incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%. ")