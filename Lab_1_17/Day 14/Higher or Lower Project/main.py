import random
import art
from game_data import data

current_score = 0
def compare(choice):
    global game
    global current_score
    if choice == 'A':
        if option_a['follower_count'] > option_b['follower_count']:
            current_score += 1
            print(f'You\'re right! Current score {current_score}')
            print(20 * '\n')
        else:
            print(f'Sorry, that\'s wrong. Final score: {current_score}')
            game = False
    else:
        if option_a['follower_count'] < option_b['follower_count']:
            current_score += 1
            print(f'You\'re right! Current score {current_score}')
            print(20 * '\n')
        else:
            print(f'Sorry, that\'s wrong. Final score: {current_score}')
            game = False

option_b = random.choice(data)
game = True
while game:
    print(art.logo)
    option_a = option_b
    option_b = random.choice(data)
    while option_a == option_b:
        option_b = random.choice(data)

    print(f'Compare A: {option_a['name']}, a {option_a['description']}, from {option_a['country']}')
    print(option_a['follower_count'])
    print(art.vs)
    print(f'Compare B: {option_b['name']}, a {option_b['description']}, from {option_b['country']}')
    print(option_b['follower_count'])

    choose = input('Type \'A\' or \'B\': ').upper()
    compare(choose)



