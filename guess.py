import random

lower_bound = 1
upper_bound = 100
target_number = random.randint(lower_bound, upper_bound)

while True:
    guess = int(input(f"Guess a number between {lower_bound} and {upper_bound}: "))
    if guess == target_number:
        print("You guessed correctly.")
        break
    elif guess < target_number:
        print("Try a higher number.")
    else:
        print("Try a lower number.")
