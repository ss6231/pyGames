
# This is a hangman game that uses an external words.txt file that is imported via the readlines() method
def mult(number):
    while (number<2) or (number>10):
        print("Invalid input")
    if (2<=number<=10):
        for mult in range (1,number+1):
            for num in range (1,number+1):
                print (mult*num,"\t",end=" ")
            print ()
print ("\n")

# Defining main function
def main():
    number = int(input("Enter number between 2 and 10 inclusive: "))
    mult (number)

main ()

# Part 2

# Define random number function
def randomnum (q):
    while (q.lower()=="yes"):
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
    
# Define main function
def main():
    q = input("Would you like to play the game? ")
    while (q.lower() != "yes") and (q.lower()!= "no"):
        print ("Invalid input")
        q = input("Would you like to play the game? ")
    randomnum(q)
        

main ()

# Part 3

# Define line function
def line (x):
    for line in range (28): 
        print ("*",end="")
    print ()

# Define checkerboard function
def checker (x):
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
        
# Define triangle function
def triangle (x):
    for row in range (1,4):
        for repeat in range (1,8):
            for st in range (row):
                print("x",end="")
            for sp in range (row,4):
                print(" ",end="")
        print ()
                
# Define diamond function
def diamond (x):
    for row in range (1,6): 
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

# Define main function
def main ():
    line ("*")
    checker ("x")
    line ("*")
    triangle ("x")
    line ("x")
    diamond ("x")
    line ("x")
    triangle ("x")
    checker ("x")
    line ("*")

main ()

