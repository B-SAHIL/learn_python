#Step 5

import random
from hungman import word_list
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)

end_of_game = False
lives = 6
from hungimage import logo
print(f"its a start of game{logo}" )
#Testing code"
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print("you have already gueesed this word:")

#Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
        lives -= 1
        print(f"wrong letter you have lose one life {guess}")
    if lives == 0:
        end_of_game = True
        print("You lose.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    from hungimage import stages
    print(stages[lives])