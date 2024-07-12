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
game_images = [rock, paper, scissors]

user_choice = int(input("Please enter a number. Type 0 for Rock, 1 for Paper or 2 for Scissors:\n"))
if user_choice >= 3 or user_choice < 0: 
  print("Invalid input, you lose! The number must be 0, 1, or 2") 
else:
  print(f'Your choice: \n {game_images[user_choice]}')
  
  computer_choice = random.randint(1,3)
  print(f"Computer choice: \n {game_images[computer_choice]}")
  
  if user_choice == 0 and computer_choice == 2:
      print("You win!")
  elif computer_choice == 0 and user_choice == 2:
      print("You lose")
  elif computer_choice > user_choice:
      print("You lose")
  elif user_choice > computer_choice:
      print("You win!")
  elif computer_choice == user_choice:
    print("It's a draw")