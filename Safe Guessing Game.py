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