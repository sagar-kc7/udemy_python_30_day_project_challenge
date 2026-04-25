import random
import sys
from art import logo

print(logo)
cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

your_cards = []
computer = []

if play == 'y':
    your_cards = random.choices(cards, k=2)
    print(f'Your cards: {your_cards}, current score= {your_cards[0] + your_cards[1]}')

    computer = random.choices(cards, k=2)
    if (computer[0] + computer[1]) == 21 :
        print('Blackjack!!! Computer\'s won')
        print(computer)
    else:
        print(f'Compute\'s first card: {computer[0]}')
elif play == 'n':
    sys.exit()

else:
    print('Please enter a valid letter which in \'y\' or \'n\' ')
    sys.exit()


def again(draw):
    # global computer
    if draw == 'y':
        your_cards.append(random.choice(cards))
        print(your_cards)
        y_score = sum(your_cards)
        print('Current scores: ', y_score)
        if sum(your_cards) > 21:
            print("You lose")
            print("Your cards sum is more than 21. It\'s ", sum(your_cards))
        elif sum(your_cards) == 21 and sum(computer) == 21:
            print('Draw')
        elif sum(your_cards) == 21:
            print('You won.........')

    elif draw == 'n':
        y_score = sum(your_cards)
        print(f'Your final hand: {your_cards}, final score: {sum(your_cards)}')
        while (sum(computer)) < 17:
            computer.append(random.choice(cards))

        c_score = sum(computer)
        print(f'Computer\'s final hand: {computer} final score: {c_score}')
        win = True
        while win:
            if c_score > 21:
                print('Opponent went over. You win 😁')
                win = False
            elif c_score > y_score:
                print("Computer\'s won")
                win = False
                break
            else:
                print('You won............')
                win = False
                break

    return again

draw_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
again(draw_again)

if (sum(your_cards)) < 21:
    draw_again = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    again(draw_again)

# play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
# if play_again == 'y':
#     print('\n' * 10)
#     print(logo)
