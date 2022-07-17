print("welcome to our shop.")
milk = int(input("how many packets of milk you want?  "))
price_of_milk = 27 * milk
bread = (input("want to buy bread also, Y or N?" ))
if bread == "Y":
    price_of_milk += 45
    print(price_of_milk)