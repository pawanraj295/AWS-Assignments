import random

def cows_and_bulls():
    # Generate a random 4-digit number
    number = str(random.randint(1000, 9999))
    print("Welcome to the Cows and Bulls Game!")
    print("Guess the 4-digit number.")
    print("For each correct digit in the correct position, you'll get a cow.")
    print("For each correct digit in the wrong position, you'll get a bull.")

    attempts = 0
    while True:
        guess = input("Enter your guess: ")

        # Check if the guess is valid
        if len(guess) != 4 or not guess.isnumeric():
            print("Invalid guess. Please enter a 4-digit number.")
            continue

        attempts += 1
        cows = 0
        bulls = 0

        # Check for cows and bulls
        for i in range(4):
            if guess[i] == number[i]:
                cows += 1
            elif guess[i] in number:
                bulls += 1

        print(f"Cows: {cows}")
        print(f"Bulls: {bulls}")

        # Check if the guess is correct
        if cows == 4:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
cows_and_bulls()