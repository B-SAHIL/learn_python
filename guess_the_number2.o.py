import random
# these are known as global constant :
EASY_LEVEL_TURN = 10
HARD_LEVEL_TURN = 5
#  create a function to check the user answer against computer number:
def check_awnser(user_guess, awnser,turn):
    if user_guess > awnser:
        print("too high: try again;; ")
        return turn - 1
    elif user_guess < awnser:
        print("too low: try again;;")
        return turn - 1
    else:
        print(f"you guessed awnser {awnser}  right  you win")

# create a fuction to set the difficulty level called difficulty_level() :
def difficulty_level():
    difficulty_choice = input("you want to play 'easy or 'hard' ? : \n ").lower()
    if difficulty_choice == 'easy':
        return EASY_LEVEL_TURN
    else:
        return HARD_LEVEL_TURN

def game():
    # game starting code  that we need to start  the game :
    from logo_guess_number import logo
    print(logo)
    print("welcome to number guess game")
    print("your number is between the range of  1 to 100 ")
    computer_choice = random.randint(1, 100)
    print(computer_choice)
    user_guess = 0
    turn = difficulty_level()
    while user_guess != computer_choice:
        print(f"youi have only {turn} attemptes")
        user_guess = int(input("guess a number? "))
        check_awnser(user_guess, computer_choice, turn)
        turn = check_awnser(user_guess, computer_choice, turn)
        #  create the function to keep the track of user lives:
        if turn == 0:
            print("you lose you are out of turns:")
            return
game()





