print("Welcome to my computer quiz! ")
t = 0
playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay! Lets's Play :) ")

print("First Question - ")
answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    t +=1
    print("Correct Answer :) ")
else:
    print("Wrong Answer :| ")

print("Second Question - ")
answer = input("What is the full form of CU? ")
if answer == "control unit":
    t +=1
    print('Correct answer :) ')
else:
    print("Wrong answer :| ")

print("Third Question - ")
answer = input("What is the brain of the computer? ")
if answer.lower() in ["cpu","central processing unit"]:
    t +=1
    print('Correct answer :) ')
else:
    print("Wrong answer :| ")

print("Fourth Question - ")
answer = input("How many bits are there in one byte? ")
if answer == "8":
    t +=1
    print('Correct answer :) ')
else:
    print("Wrong answer :| ")

print("Fifth Question - ")
answer = input("What is the smallest unit of data in a computer? ")
if answer.lower()== "bit":
    t +=1
    print('Correct answer :) ')
else:
    print("Wrong answer :| ")
if t > 2:
    print("Congratulations,You have got ",t,"answers correct !")
else:
    print(f"You got only {t} answers correct :( \nBetter luck next time !!")
