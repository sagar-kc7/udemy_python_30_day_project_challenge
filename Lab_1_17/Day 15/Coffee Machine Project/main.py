MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def make(choosen_item):
    global money
    if choosen_item == 'espresso':
        if resources['water'] >= 50 and resources['coffee'] >=18:
            resources['water'] -= 50
            resources['coffee'] -= 18
            money += 1.5
            return True
        else:
            print('Sorry there is not enough water.')
            return False

    elif choosen_item == 'latte':
        if resources['water'] >= 200 and resources['milk'] >= 150 and resources['coffee'] >= 24:
            resources['water'] -= 200
            resources['milk'] -= 150
            resources['coffee'] -= 24
            money += 2.5
            return True
        else:
            print('Sorry there is not enough water.')
            return False

    elif choosen_item == 'cappuccino':
        if resources['water'] >= 250 and resources['milk'] >= 100 and resources['coffee'] >= 24:
            resources['water'] -= 250
            resources['milk'] -= 100
            resources['coffee'] -= 24
            money += 3.0
            return True
        else:
            print('Sorry there is not enough water.')
            return False

    if choosen_item == 'report':
        for key, value in resources.items():
            print(f'{key}: {value}')
        print(f'money: {money}')
    return True

def coins(choosen_item):
    if choosen_item == 'report':
        return True
    else:
        print('Please insert coins.')
        target = MENU[choosen_item]['cost']
        quarters = 0.25* float(input('how many quarters?: '))
        dimes = 0.10* float(input('how many dimes?: '))
        nickles = 0.05* float(input('how many nickles?: '))
        pennies = 0.01* float(input('how many pennies?: '))
        sums = quarters+dimes+nickles+pennies

        if sums >= target :
            refund = sums - target
            print(f'Here is ${refund:.2f} in change.')
            print(f'Here is your {[choosen_item]} ☕️. Enjoy!')
            return True
        else:
            print('Sorry that\'s not enough money. Money refunded.')
            return False

money = 0
game = True
while game:
    choose = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choose == 'off':
        game = False
    elif make(choose):
        coins(choose)

