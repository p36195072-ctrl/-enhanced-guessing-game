# -enhanced-guessing-game
Safe Guessing Game

A beginner-friendly Python project that demonstrates how to create a number guessing game with error handling.

📌 Description

This program:

Generates a random secret number between 1 and 10
Continuously asks the user to guess the number
Gives hints if the guess is too high or too low
Handles invalid input using try-except
Stops only when the correct number is guessed

🧠 Concepts Used

while True loop
if-elif-else conditions
try-except
ValueError
random module
randint() function
User Input
break statement

💻 Code

import random

secret = random.randint(1, 10)

while True:
    try:
        guess = int(input("Enter your number: "))

        if guess == secret:
            print("Correct guess")
            break

        elif guess < secret:
            print("Low! Try again")

        else:
            print("High! Try again")

    except ValueError:
        print("Invalid input")

▶️ Example Output

Enter your number: 3
Low! Try again

Enter your number: hello
Invalid input

Enter your number: 8
Correct guess
