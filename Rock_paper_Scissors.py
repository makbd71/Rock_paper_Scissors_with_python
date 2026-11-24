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

options = [rock, paper, scissors]

player_pick = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))

if player_pick < 0 or player_pick > 2:
    print("Invalid number. You lose!")
else:
    print("You picked:")
    print(options[player_pick])

    computer_pick = random.randint(0, 2)
    print("Computer picked:")
    print(options[computer_pick])

    if player_pick == computer_pick:
        print("Tie!")
    elif (player_pick == 0 and computer_pick == 2) or \
         (player_pick == 1 and computer_pick == 0) or \
         (player_pick == 2 and computer_pick == 1):
        print("You win!")
    else:
        print("You lose!")