🎯 Number Guessing Game
A simple and fun command-line Number Guessing Game written in Python. The program generates a random number between 1 and 100, and the player tries to guess it in as few attempts as possible.

📌 Description
This game challenges the player to guess a randomly generated number within a specified range. After each guess, the program provides feedback:

📈 "Higher than that! Try again." — if the guess is too low
📉 "Lower than that! Try again." — if the guess is too high
🎉 "Congratulations!" — when the correct number is guessed

The game also tracks the number of attempts and allows the player to replay as many times as they like.

✨ Features
Random number generation between 1 and 100
Input validation for out-of-range guesses
Attempt counter
Replay option
Clear and interactive user feedback

🧠 Game Logic Overview
A random number is generated using Python’s random module.
The player is prompted to enter guesses.
The program compares the guess with the generated number.
The loop continues until the correct number is guessed.
After completion, the total number of attempts is displayed.
The player can choose to play again or exit.

📂 Project Structure
Number Guessing Game
│── guessing_game.py
│── README.md


👤 Author
Mohammed Muien