# dispaly art, get random acounnt, printable formet , guess, follower, check, awnser, repatabler
import random
from logo_higher_lower import logo
from logo_higher_lower import vs
from data_higher_lower import data
current_score = 0
print(logo)
should_continew = True


def get_random_acounnt():
    random_choice = random.choice(data)
    return random_choice
b_acounnt = get_random_acounnt()

while should_continew:
    a_acounnt = b_acounnt
    b_acounnt = get_random_acounnt()
    def formeted_data(acounnt):
        name = acounnt['name']
        description = acounnt['description']
        country = acounnt[ 'country']
        return  (f"{name} {description}, from {country} ")
    def check_answer(guess, a_follower, b_follower):
        if a_follower > b_follower:
            return guess == 'a'
        else:
            return guess == 'b'
    print(f"compare 'A': {formeted_data(a_acounnt)}")
    print(vs)
    print(f"against 'B': {formeted_data(b_acounnt)}")
    guess = input("who has a more follower 'a' or 'b'? :\n ").lower()
    # check answer
    # get follower  count
    a_follower = a_acounnt['follower_count']
    b_follwer = b_acounnt['follower_count']
    is_corrrect = check_answer(guess, a_follower, b_follwer)
    if is_corrrect:
        current_score += 1
        print(f"you are right your curennt score is {current_score}:")
    else:
        should_continew = False
        print(f"sorry you are wrong: your current score of {current_score}::")