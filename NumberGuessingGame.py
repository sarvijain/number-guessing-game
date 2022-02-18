import random

print("Number guessing game")
number = random.randint(1, 9)
chances = 0
print("Guess a number (between 1 and 9)")

while chances < 5:
    guess = int(input("Enter your guess:"))

    if guess == number:
        print("CONGRATULATIONS YOU WON!!!!")
        break

    elif guess < number:
        print("your guess was too low: guess a number higher than", guess)

    else:
        print("your guess was too high: guess a number lower than", guess)

    chances += 1

if  not chances > 5:
    print("YOU lose !!! The number is ", number)
