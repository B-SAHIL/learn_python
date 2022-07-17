# Create a function in Python that accepts two parameters.
# The first should be the full price of an item as an integer.
# The second should be the discount percentage as an integer.
#
# The function should return the price of the item after the discount has been applied.
# For example, if the price is 100 and the discount is 20, the function should return 80.
total_bill = int(input("enter your total bill amounnt? ;\n"))
discount = int(input("enter the percentage you want to discouunt?:\n"))
# divide = discount / total_bill
# percentage = divide * 100
# bill_after_discount = total_bill - percentage
# print(bill_after_discount)
def bill_after_discount(x,y):
  discounted_price = (x*y)/100
  total_price = x - discounted_price
  return total_price

print(f"your bill after discount is ${bill_after_discount(total_bill, discount)}")