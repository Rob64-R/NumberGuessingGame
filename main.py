import random
import math

print("Please input range")

lower = int(input("Enter the lower limit: "))
upper = int(input("enter the upper limit: "))

x = random.randint(lower, upper)
condition = math.log(upper - lower + 1,2)
tries = round(condition)
print("You only have ", round(condition), " chances to guess the number!")

count = 0

while count < tries:
    count += 1

    guess = int(input("Guess a number: "))

    if x == guess:
        print("Congratulations!")
        print("You guessed in", count, "try/tries")
        break
    elif x > guess:
        print("Guess is too low!")
        print("Guesses remaining:", tries - count)
    elif x < guess:
        print("Guess is too high!")
        print("Guesses remaining:", tries - count)

if count >= tries:
    print("The number was:", x)
    print("Too Bad!")