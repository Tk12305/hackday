import random
def guess_the_number():
    user_wants_to_stop = 0

    while True:
        if user_wants_to_stop:
            break
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
                    # If the guess is correct, break out of the loop
                    print(f"Congratulations! You guessed the number.")
                    break
            except ValueError:
                print("Please enter a valid number.")


        # Ask if the player wants to play again
        play_again = input("Do you want to play again? (yes or no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye!")
            user_wants_to_stop = 1


# Run the game
guess_the_number()