###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you

# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!

# Generate a random number to guess
import random
digits = list(range(10))
random.shuffle(digits)
guess_number = digits[:3]
print('Random number is {}'.format(guess_number))

# Start game and ask to user start guessing
print ("Welcome to Code Breaker! Let's see if you can guess my 3 digit number!\n Code has been generated, please guess a 3 digit number")

play_game = True  # Play game while this condition is true

while (play_game):
    check = []   # Check for guesses
    user_guess = input("What is your guess? ")
    # Convert user guess to an int list for direct comparison with our guess number, also an int list
    user_guess_list = [int(i) for i in str(user_guess)]

    if 3 < len(user_guess_list) > 3:
        print ('Guess number must be 3 digits exactly, try again......')

    else:
        for i in range(3):
            if user_guess_list[i] in guess_number and guess_number.index(user_guess_list[i]) == i:
                # append 2 for digit correctly guessed and in the right position
                check.append(2)
            
            elif user_guess_list[i] in guess_number and guess_number.index(user_guess_list[i]) != i:
                # append 1 for digit correctly guessed but in the wrong position
                check.append(1)
                
            elif user_guess_list[i] not in guess_number:
                # append 0 for digit wrongly guessed
                check.append(0)

        if user_guess_list == guess_number:
            play_game = False

        elif  2 in check:
            print ("Match: You've guessed a correct number in the correct position")
        
        elif 1 in check:
            print ("Close: You've guessed a correct number but in the wrong position")

        else:       
            print ("Nope: You haven't guess any of the numbers correctly")
    
    print('Check is currently {}'.format(check))

print_guess_number = int(''.join([str(i) for i in guess_number]))
print("Game over! You have correctly guessed my 3 digit number: {}".format(print_guess_number))

''' Solution Notes: 
    1. Break down logic into functions i.e get input, generate guess number, game logic etc
    2. EXPLORE enumerate() that can compare both a number and its index in the for loop in one go       ie. for index, num in enumerate(user_guess): if num == code[index], uses tuple unpacking '''