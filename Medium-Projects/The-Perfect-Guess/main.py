# A Number Guessing Game

import random

def random_number():
    return random.randint(1, 100)

while True:
    num = random_number()
    print("Welcome to the Number Guessing Game!")
    g = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < 1 or guess > 100:
            print("Please guess a number within the range of 1 to 100.")
            continue
        g += 1
        if guess < num:
            print("Higher than that! Try again.")
        elif guess > num:
            print("Lower than that! Try again.")
        else:
            print("Congratulations! You've guessed the number!")
            break
    print(f"The correct number was: {num}")
    print(f"You guessed the number in {g} attempts.")
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again == 'n':
        print("Thanks for playing! Goodbye!")
        break