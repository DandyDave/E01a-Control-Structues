#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                 #print Greetings! to the console.
colors = ['red','orange','yellow','green','blue','violet','purple']                               #colors is a list
play_again = ''                                                                                   # Creation of the play_again variable
best_count = sys.maxsize                                                                          # the biggest number
while (play_again != 'n' and play_again != 'no'):                                                 # while funccction which checks if the user answered yes or no to play again.
    match_color = random.choice(colors)                                                           # random.choice chooses a random string from the list of colors which is then assigned to the variable match_color.
    count = 0                                                                                     # the variable count being created and being set to 0
    color = ''                                                                                    # the variable being created
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")                                            # \n is a special code that adds a new line / users input for color
        color = color.lower().strip()                                                             # The string in color is being lowercased and striped of its spaces.
        count += 1                                                                                # Adds 1 to the variable count every time the statement runs.
        if (color == match_color):                                                                # An if statement that checks if color input equals match_color
            print('Correct!')                                                                     # Prints correct
        else:                                                                                     # Beginning of else statement
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))    # Prints message and format inserts number of guesses into {}
    print('\nYou guessed it in {0} tries!'.format(count))                                         # Prints how many times the user has guessed wrong
    if (count < best_count):                                                                      # Checks if the current count is lower than the best_count
        print('This was your best guess so far!')                                                 # Prints messgage
        best_count = count                                                                        # Updates best_count to the value of current count
    play_again = input("\nWould you like to play again? ").lower().strip()                        # Input where the user decides if they want to play again.
print('Thanks for playing!')                                                                      # prints message