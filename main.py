#pizza = 15 , 20 , 25
#mediume and large pizza have the same prize fro topping
#pepproni = 2 , 5
#cheese = 2
print("welcome to python pizza delhivery.:)")
size = input("what size of pizza do you want? S,M,L? ")
add_pepproni = input("do you want pepproni? Y or N? ")
extra_cheese = input("do you want extra cheese? Y or N ? ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepproni == 'Y':
    if size == "S":
        bill += 2
    else: bill += 3

if extra_cheese == "Y":
    bill += 2
print(F"your total bill is ${bill}, ")






