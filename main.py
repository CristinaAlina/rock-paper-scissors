import random

# declare the ascii art for each game option
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

# declare a list with the game options
options = [rock, paper, scissors]

user_choice = input(
    'What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n')

if user_choice in ["0", "1", "2"]:

    user_choice_int = int(user_choice)
    option_user = options[user_choice_int]

    print(option_user)

    computer_choice_int = random.randint(0, 2)
    option_computer = options[computer_choice_int]

    print(f'Computer chose:\n{option_computer}')

    if user_choice_int == computer_choice_int:
        print('It\'s a draw!')
    elif user_choice_int == 0 and computer_choice_int == 2:
        # if user chose rock(0) and computer scissors(2)
        print('You win!')
    elif user_choice_int == 2 and computer_choice_int == 0:
        # if user chose scissors(2) and computer rock(0)
        print('You lose!')
    elif user_choice_int > computer_choice_int:
        # if (paper(1) and rock(0)) or (scissors(2) and paper(1))
        print('You win!')
    else:
        # if (rock(0) and paper(1)) or (paper(1) and scissors(2))
        print('You lose!')

else:
    print(f'Your option "{user_choice}" is invalid. You lose!')
