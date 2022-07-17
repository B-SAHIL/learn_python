import  random


def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


player_card = []
compuetr_card = []


for _ in range(2):
  player_card.append(deal_card())
  print(f"user_card {player_card}")
  compuetr_card.append(deal_card())
  print(f"compuetr_card  is {compuetr_card[0]}")


def calculator(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)
#HinXXLLLt 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and
# return 0 instead of the actual score. 0 will represent a blackjack in our game.
def play_game():
  end_game = False
  while not end_game:
    user_score = calculator(player_card)
    print(f"user_score {user_score}")
    computer_score = calculator(compuetr_card)
    print(f"computer_score {computer_score}")
    if user_score == 0 or computer_score == 0 or user_score > 21:
      end_game = True
    else:
      new_card = input("user want to drow new card 'yes' or 'no'")
      if new_card == 'yes':
        player_card.append(deal_card())
        calculator(player_card)
      else: end_game = True

  while computer_score != 0 and computer_score < 17:
    compuetr_card.append(deal_card())
    computer_score = calculator(compuetr_card)


  def compare(user_score,computer_score):
    if user_score == computer_score:
      print("it's a draw")
    elif user_score == 21:
      print("user win ")
    elif computer_score == 0:
      print("computer win:")
    elif user_score == 0:
      print("user win:")
    elif user_score > 21:
      print("computer winns ")
    elif  computer_score > 21:
      print("user win")
    elif user_score > computer_score:
      print("user win:")
    else: print("computer win ")
  compare(user_score , computer_score)
play_game()
restart = input("you want to restart 'yes' or 'no' ?" )
if restart == 'yes':
    play_game()


