# branch.py

a = 4
b = 5
c = 7

if a % 2:
    print(a, '为奇数')

if b % 2:
    print(b, '为奇数')

if c % 2:
    print(c, '为奇数')


x = 3

if x > 0:
    print("Positive")
if x < 0:
    print("Negative")
if x == 0:
    print("Zero")

if x > 0:
    print("Positive")
else:
    if x < 0:
        print("Negative")
    else:
        if x == 0:
            print("Zero")

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
elif x == 0:
    print("Zero")

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")


percent = float(input("What percentage did you earn? "))

if percent >= 90:
    print("You got an A!")

if percent >= 80:
    print("You got a B!")

if percent >= 70:
    print("You got a C!")

if percent >= 60:
    print("You got a D!")

if percent < 60:
    print("You got an F!")


percent = float(input("What percentage did you earn? "))
assert 0 <= percent <= 100, 'invalid percent'

if percent >= 90:
    print("You got an A!")
else:
    if percent >= 80:
        print("You got a B!")
    else:
        if percent >= 70:
            print("You got a C!")
        else:
            if percent >= 60:
                print("You got a D!")
            else:
                if percent < 60:
                    print("You got an F!")


percent = float(input("What percentage did you earn? "))
assert 0 <= percent <= 100, 'invalid percent'

if percent >= 90:
    print("You got an A!")
elif percent >= 80:
    print("You got a B!")
elif percent >= 70:
    print("You got a C!")
elif percent >= 60:
    print("You got a D!")
else: # percent < 60
    print("You got an F!")
    


# betting code (unfactored redundant version)
if money < 500:
    print("You have $", money, "left.")
    print("Cash is dangerously low. Bet carefully.")
    bet = int(input("How much do you want to bet?"))
elif money < 1000:
    print("You have $", money, "left.")
    print("Cash is somewhat low. Bet moderately.")
    bet = int(input("How much do you want to bet?"))
else:
    print("You have $", money, "left.")
    print("Cash is in good shape. Bet liberally.")
    bet = int(input("How much do you want to bet?"))

print("You have $", money, "left.")
if money < 500:
    print("Cash is dangerously low. Bet carefully.")
elif money < 1000:
    print("Cash is somewhat low. Bet moderately.")
else:
    print("Cash is in good shape. Bet liberally.")
bet = int(input("How much do you want to bet?"))

