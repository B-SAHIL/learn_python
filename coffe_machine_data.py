MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


PROFIT = 0
def coin_total():
    ''''this function calculate the value of coins to get total'''

    print("plase enter the coins")
    total = int(input("how many quarters? : ")) * 0.25
    total += int(input("how many dimes? : ")) * 0.1
    total += int(input("how many nickles? : ")) * 0.05
    total += int(input("how many pennies? :")) * 0.01
    return total


def is_transaction_successful(price_of_drink, money_recived ):
    '''' this function is use to check the transaction is successful or not '''
    if price_of_drink > money_recived:
        print("you have entered insufficient amount: money refunded ")
    elif price_of_drink <= money_recived:
        change = money_recived - price_of_drink
        print(f"here is your change {change}")
        global PROFIT
        PROFIT += money_recived
        return True
    elif price_of_drink > money_recived:
        return False


def check_resources(order_ingerdintes):
    ''' this function is use to check that resources are enough for making drink or not '''
    for item in order_ingerdintes:
        if resources[item] < order_ingerdintes[item]:
            return False

        else: return True

def make_coffe(choice, order_ingerdintes):
    for item in order_ingerdintes:
        resources[item] -= order_ingerdintes[item]
    print(f"here is you {choice} enjoy:: ")

should_continew = True
while should_continew:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "of":
        should_continew = False
    elif choice == "report":
        print(f'water in machine {resources["water"]}ml: ')
        print(f'milk in machine {resources["milk"]}ml: ')
        print(f'coffee in machine {resources["coffee"]}ml: ')
    else:
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):
            payment = coin_total()
            if is_transaction_successful(drink["cost"], payment):
                make_coffe(choice, drink["ingredients"])


