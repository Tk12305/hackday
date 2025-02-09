import random
def guess_the_number():
    while True:
        print("Welcome to 'Guess the Number'!")
        print("I’m thinking of a number between 1 and 1000.")

        # The computer picks a random number between 1 and 100
        secret_number = random.randint(1, 1000)

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
                    # If the guess is correct, break out of the loop
                    print(f"Congratulations! You guessed the number.")
                    break
            except ValueError:
                print("Please enter a valid number.")


# Run the game
guess_the_number()