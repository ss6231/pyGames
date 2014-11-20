'''
First part of this program prints out formatted multiplication tables

Second part has another random number guessing game and prints out the number of trials left if the guess is incorrect

Last part prints out a printed "carpet" using nested loops and various characters
'''

# Part 1

number = int(input("Enter number between 2 and 10 inclusive: "))
while (number<2) or (number>10):
    print("Invalid input")
    number = int(input("Enter number between 2 and 10 inclusive: "))
if (2<=number<=10):
    for mult in range (1,number+1):
        for num in range (1,number+1):
            print (mult*num,"\t",end=" ")
        print ()
print ("\n")

# Part 2

q = input("Would you like to play the game? ")
while (q != "yes") and (q!="Yes") and (q!= "no") and (q!= "No"):
    print ("Invalid input")
    q = input("Would you like to play the game? ")
while (q == "yes" or q == "Yes"):
    chance = 3
    import random
    num = random.randint (10,99)
    for trial in range (3):
        guess = int(input("Guess the two digit number: "))
        if guess == num:
            print ("Congrats you win!")
            break
        elif guess != num and chance > 1:
            print ("Incorrect! You have",chance-1,"chance(s) left")
        elif guess != num and chance == 1:
            print ("Incorrect! You lose the game!")
        chance = chance - 1 
    q = input("Would you like to play the game? ")
print("\n")

# Part 3


for line in range (28): # line of *'s
        print ("*",end="")
print ()
    
for repeat in range (2):    
    for pattern in range (7):
        for star in range (2):
            print ("x",end="")
        for space in range (2):
            print(" ",end="")
    print()
    for pattern2 in range (7):
        for space2 in range (2):
            print (" ",end="")
        for star2 in range (2):
            print ("x",end="")
    print()
    
for line in range (28): # line of *'s
        print ("*",end="")
print ()
    
for row in range (1,4): # triangle 
    for repeat in range (1,8):
        for st in range (row):
            print("x",end="")
        for sp in range (row,4):
            print(" ",end="")
        
    print() # line of *'s
for star in range (28):
    print("*",end="")
print()

for row in range (1,6): # diamond
    for col in range (8):
        print(" ",end="")
    for sp in range (row,5):
        print(" ",end="")
    for st in range (row):
        print("x",end="")
    for st2 in range (row-1):
        print("x",end="")
    print()
for row in range (1,5):
    for col in range (8):
        print(" ",end="")
    for sp in range (row):
        print(" ",end="")
    for st in range (row,5):
        print("x",end="")
    for st2 in range (row+1,5):
        print("x",end="")
    print()

for star in range (28):
    print("*",end="")
print()

for row in range (1,4): # triangle pattern 
    for repeat in range (1,8):
        for st in range (row):
            print("x",end="")
        for sp in range (row,4):
            print(" ",end="")
    print()
    
for line in range (28): # line of *'s
        print ("*",end="")
print ()

for repeat in range (2):    # checkerboard pattern
    for pattern in range (7):
        for star in range (2):
            print ("x",end="")
        for space in range (2):
            print(" ",end="")
    print()
    for pattern2 in range (7):
        for space2 in range (2):
            print (" ",end="")
        for star2 in range (2):
            print ("x",end="")
    print()
    
for line in range (28): # line of *'s
        print ("*",end="")
print ()

