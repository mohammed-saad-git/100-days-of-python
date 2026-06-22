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





#adding the already assigned variables to the list
game_images=[rock,paper,scissors]

user_input=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_input>=0 and user_input<=2:
    print(game_images[user_input])

computer_choice=random.randint(0 , 2)
print(f"computer choose")
print(game_images[computer_choice])
if user_input>=3 or user_input <0:
    print("you have chosen a wrong value")

elif user_input==0 and computer_choice==2:
    print("you won")

elif computer_choice==0 and user_input==2:
    print("you Loose")

elif computer_choice>user_input:
    print("you loose")

elif user_input>computer_choice:
    print("you won")

elif computer_choice==user_input:
    print("its a draw")
