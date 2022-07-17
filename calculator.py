from calculato_logo import logo
def add(x, y):
  return x + y


def sub(x, y):
  return x - y


def devide(x, y):
  return x / y


def multiply(x, y):
  return x * y


oprations = {"+": add,
             "-": sub,
             "/": devide,
             "*": multiply
             }
def calx():
  print(logo)
  number_1 = float(input("enter your first number? : \n"))
  for key in oprations:
    print(key)

  should_continew  = False
  while not should_continew:
      user_want = input("pick one of the opration from the opration?: \n ")
      number_2 = float(input("enter your next number? : \n"))
      answer = oprations[user_want]
      answer = answer(number_1,number_2)
      print(f"{number_1} {user_want} {number_2} = {answer}")
      continew = input("onther calx? 'y' or 'n'")
      if continew == 'y':
        number_1 = answer
      elif continew == 'n':
        should_continew = True
        calx()

calx()

