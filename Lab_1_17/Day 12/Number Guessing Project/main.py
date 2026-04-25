import random
from art import logo
import sys

print(logo)
print('Welcome to the Number Guessing Game!\nI\'m thinking of a number between 1 and 100.')
random_choose = random.randint(1, 101)
print(random_choose)
difficulty = input('Choose a difficulty. Type \'easy\' or \'hard\': ').lower()

if difficulty == 'easy':
    number_of_guess = 10
else:
    number_of_guess = 5

def check(num):
    global number_of_guess
    if num> 100 or num < 1:
        print('Please enter the number between 1 and 100!!!!')
        sys.exit()
    elif num == random_choose:
        print(f'You got it! The answer was {num}')
        number_of_guess = 0
    else:
        if number_of_guess > 1:
            if num > random_choose:
                print('Your number is high.')
            else:
                print('Your number is less')
            print('Guss again')
            number_of_guess -= 1
        else:
            print('Game over')
            number_of_guess -= 1
            print('The number is', random_choose)

print(number_of_guess)
while number_of_guess != 0 :
    print(f'You have {number_of_guess} attempts remaining to guess the number')
    guess = int(input('Make a guess: '))
    check(guess)
