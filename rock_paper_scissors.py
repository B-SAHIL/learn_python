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
---.__________)'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game_image = [rock, paper, scissors]
player_choice = int(input("chosse in between rock(0) , paper(1) scissors (2)? "))
print(game_image[player_choice])
computer_choice = random.randint(0, 2)
print(game_image[computer_choice])
if player_choice == computer_choice:
    print("you lose cause you chosse wrong number")
elif player_choice == 1 and computer_choice == 2:
    print("you lose!!!")
elif player_choice == 2 and computer_choice == 1:
    print("you win !! ")
elif player_choice == 0 and computer_choice == 1:
    print("you lose!!!")
elif player_choice == 1 and computer_choice == 0:
    print("you win !!")
elif player_choice == 2 and computer_choice == 0:
    print("ypu win!!")
elif player_choice == 0 and computer_choice == 2:
    print("you lose!! ")



