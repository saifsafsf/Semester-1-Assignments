import random   # Importing Module
randint = random.randint(1, 1000)   # Generating Random Number
print('Let\'s play a game. Guess what number have I chosen for you from 1 to 1000.')
num = int(input('Enter your guess from 1 to 1000: '))    # Taking Input
while num != randint:   # If guess is not correct
    if 1 > num > 1000:  
        print('Invalid Input... Try entering a number between the limits mentioned.\n')
    elif num >= randint + 200:
        print('Try HARDER! Your guessed number is "Too High"!\n')
    elif num <= randint - 200:
        print('Try HARDER! Your guessed number is "Too Low"!\n')
    elif num >= randint + 10:
        print('A bit far! Your guessed number is "High"!\n')
    elif num <= randint - 10:
        print('A bit far! Your guessed number is "Low"!\n')
    elif num > randint:     # if one of the upper conditions are not true, then guess is 10 values high
        print('Close! Your guessed number is "Slightly High"!\n')
    elif num < randint:     # if one of the upper conditions are not true, the guess is 10 values low
        print('Close! Your guessed number is "Slighly Low"!\n')
    else:
        pass
    num = int(input('Enter a number from 1 to 1000: '))
print('YAY! you did it! Your guessed number is "Correct"!')     # Control gets out of loop only if the guess is correct
