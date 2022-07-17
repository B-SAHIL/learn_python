bids = {}
fishied_bid = False
while not fishied_bid:
  name = input("enter your name?: \n")
  bid = int(input("enter your bid amounnt?: \n"))
  bids[name] = bid
  restart = input("if you  nay other bidder want to bid? 'yes' or 'no':")
  if restart == 'no':
    fishied_bid = True
    hihest_bid = 0
    winner = ""
    for bidder in bids:
      bid_ammount = bids[bidder]
      if bid_ammount > hihest_bid:
        hihest_bid = bid_ammount
        winner = bidder
    print(f"the heighest bidder is {winner} with the amounnt of {hihest_bid} ")


  elif restart == 'yes':
    fishied_bid = False