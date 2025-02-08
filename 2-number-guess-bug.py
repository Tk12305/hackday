import random
import time
import os

def clear_screen():
    # Clear the screen for different OS
    os.system('cls' if os.name = 'nt' else 'clear')

def celebrate():
    fireworks = [
        "        *         *",
        "       * *       * *",
        "      *   *     *   *",
        "     *     *   *     *",
        "    *       * *       *",
        "   *         *         *",
        "    *       * *       *",
        "     *     *   *     *",
        "      *   *     *   *",
        "       * *       * *",
        "        *         *"
    ]

    for _ in range(5):  # Display fireworks 5 times
        clear_screen()
        for line in fireworks:
            print(line)
        time.sleep(0.5)
        clear_screen()
        time.sleep(0.3)

    print("🎉🎉🎉 Congratulations! You guessed the number! 🎉🎉🎉")

def guess_the_number():
    while True:
        print("Welcome to 'Guess the Number'!")
        print("I’m thinking of a number between 1 and 100.")

        # The computer picks a random number between 1 and 100
        secret_number = random.randint(1, 100)

        while True:
            try:
                # Prompt the user to guess the number
                guess = int(input("Enter your guess: "))

                # Check the guess
                if guess < secret_number:
                    print("Too low! Try again.")
                elif guess > secret_number:
                    print("Too high! Try again.")
                else:
                    # If the guess is correct, celebrate and break out of the loop
                    celebrate()
                    break
            except ValueError:
                print("Please enter a valid number.")

# Run the game
guess_the_number()
