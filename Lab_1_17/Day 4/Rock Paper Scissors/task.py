import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n"))
computer = random.randint(0,2)

if choose == 0:
    print(rock)
elif choose == 1:
    print(paper)
elif choose == 2:
    print(scissors)

print('Computer chose:\n')
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

if choose == computer:
    print('TIE')
elif (choose==1 and computer ==0) or (choose == 2 and computer == 1 ) or (choose == 0 and computer == 2) :
    print('You win')
else:
    print('You lose')