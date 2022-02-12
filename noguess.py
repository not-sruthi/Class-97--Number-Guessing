#Import a random module into your file.
#Use random to generate a random number from 1-9.
#Give users 5 chances to guess the number.
#If the user guesses incorrectly, show a hint or message to the user if their guess was close or far.
#If the user guesses correctly show the congratulating message.
#Save the code.
#Run and test the code.

import random

number = random.randint(1,9)

chances= 5
while chances>0:
    guess= int(input('Guess a number from 1 to 9: '))
    if (guess==number):
        print('Congrats!')
        print()
        break
    else:
        print('Nope!')
        print()
    chances=chances-1

    if (chances==0):
        print('Too bad! The number was ',number)


