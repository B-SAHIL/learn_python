# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_str = name1 + name2
lower_combined = combined_str.lower()
t = lower_combined.count("t")
r = lower_combined.count("r")
u = lower_combined.count("u")
e = lower_combined.count("e")
true = str(t + r + u + e)
l = lower_combined.count("l")
o = lower_combined.count("o")
v = lower_combined.count("v")
e = lower_combined.count("e")
love = str(l + o + v + e)
score = (true + love)
score = int(score)
if score <10 or score >90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 or score < 50:
    print(f"Your score is {score}, you are alright together.")
else: print(f"your score is {score}.")
