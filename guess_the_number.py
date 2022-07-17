from logo_guess_number import logo
print(logo)
import random
print("welcome to guess the number game ;;;;;:")

def hard():
    computer_guess = random.randint(1, 100,)
    end_game = False
    lives = 5
    while not end_game:
        guessed_number = int(input("enter your number ? "))
        if lives < 2 :
            end_game = True
            print("you loose")
        elif guessed_number != computer_guess and guessed_number < computer_guess:
                lives  = lives - 1
                print(lives)
                print("too low : try again ")

        elif guessed_number != computer_guess and guessed_number > computer_guess:
            lives = lives - 1
            print(lives)
            print("too high try again")
        elif guessed_number == computer_guess:
            end_game = True
            print("you winn: ")
def easy():
    computer_guess = random.randint(1, 100, )
    end_game = False
    lives = 10
    while not end_game:
        guessed_number = int(input("enter your number ? "))
        if lives < 2:
            end_game = True
            print("you loose")
        elif guessed_number != computer_guess and guessed_number < computer_guess:
            lives = lives - 1
            print(lives)
            print("too low : try again ")

        elif guessed_number != computer_guess and guessed_number > computer_guess:
            lives = lives - 1
            print(lives)
            print("too high try again")
        elif guessed_number == computer_guess:
            end_game = True
            print("you winn: ")

game = input("you want to play hard or easy ? ").lower()
if game == 'easy':
    print("welcome to easy level you have 10 lives :")
    easy()
elif game == 'hard':
    print("welcome to hard level you have only 5 lives: ")
    hard()
else:
    print("invelid input try again of exit the game")

