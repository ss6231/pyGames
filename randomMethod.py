

# Part one:
chances = 3
print ("The secret number is in between 1 and 20, inclusive")
for trials in range (3):
    import random # Random function 
    num = random.randint (1,20) # Define parameters
    guess = int(input("Guess the secret number: "))
    chances = chances - 1 # accumulator for range
    if (guess==num): # Correct guess
        print ("Correct! The secret number is",num)
        break
    if (guess!=num) and (chances==0): # Incorrect guesses and no trials left
        print ("Sorry, you lost the game! No more chances left!")
    elif (guess>20) or (guess<1): # Invalid input, this counts as a trial
        print ("Invalid input. You have",chances,"trial(s) left")
    else: # Lose game
        print ("Incorrect! You have",chances,"trial(s) left")
print ("\n")


# Part two:
chances = 5
print ("The secret word is a color")
for trials in range (5):
    guess = input("Guess the secret word: ")
    chances = chances - 1 # setting accumulator
    if (guess=="blue") or (guess=="Blue"):
        print("Congrats! You win a million dollars!")
        break # stops loop if guesses correctly
    if (guess!="blue"):
        print ("Sorry! Incorrect guess! You have",chances,"trial(s) left")
print ("\n")



# Part three:
total = 0 # setting up for accumulator 
month = 0
expense = float(input("Enter your expense (or -1 to exit): "))
while (expense != -1) and (expense>0): # setting sentinel
    total = total + expense # accumulator for total
    expense = float(input("Enter your expense (or -1 to exit): "))
    month = month + 1 # accumulator for month
if (expense != 0) and (expense == -1) and (month != 0): # if 1st input -1 or 0,
                                                        # month will be 0 and
                                                        # it will not calculate
    average = total/month # calculating average
    print ("The total is",total)
    print ("The average is",average)
elif (expense == 0): # Must have an expense that isn't -1
    print ("No expense entered")
else: # No negative numbers
    print ("Invalid input")

print("\n")

# Part four:

binary = str(input("Enter a binary number: "))
while (len(binary)>8): # Only accepts 8 digit binaries
    print ("Input has more than 8 characters")
    binary = str(input("Enter a binary number: "))
num = 0 # setting accumulator 
exp = 7
for char in binary:
    num = num + int(char)*(2**exp) # binary conversion
    exp = exp - 1 # updating exponent
print ("The equivalent decimal number is",num)
print("\n")

# ascii value

word = input("Enter a word: ")
for letter in word:
    num = ord(letter) # converting original letter to ascii
    newchar = chr(num+1) # updating new character
    print ("Original letter is",letter,"and Ascii number is",ord(letter))
    print ("New letter is",newchar,"and Ascii number is",ord(newchar))


  

