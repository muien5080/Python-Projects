# Rock, Paper and Scissors Game

import random

def get_user_choice():
    print("Enter your choice (rock, paper, scissors): ")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    choice = int(input("Your choice: "))
    if choice in [1, 2, 3]:
        return choice
    else:
        print("Invalid choice!, Please enter a valid choice.")
        return get_user_choice()

def get_computer_choice():
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 1 and computer_choice == 3) or (user_choice == 2 and computer_choice == 1) or (user_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"
    
def display_choice(computer_choice, user_choice):
    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print(f"You chose: {choices[user_choice]}")
    print(f"Computer chose: {choices[computer_choice]}")
    
# Main function to run the game
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    display_choice(computer_choice, user_choice)
    result = determine_winner(user_choice, computer_choice)
    print(result)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing! Goodbye!")
        break