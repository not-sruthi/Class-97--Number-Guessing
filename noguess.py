import random

#getting random number
number = random.randint(1,9)

chances= 5

#giving user 5 chances to input correct number
while chances>0:
    guess= int(input('Guess a number from 1 to 9: '))
    
    #checking if guess is correct
    if (guess==number):
        print('Congrats!')
        print()
        break
    else:
        print('Nope!')
        print()
    chances=chances-1
    
    #fail condition
    if (chances==0):
        print('Too bad! The number was ',number)


