import random

def computer_guess_game():
    print("Think of a number between 1 and 100. I will try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0
    guessed_numbers = set()

    while True:
        guess = random.randint(low, high)
        
        # Ensure the guess hasn't been made before
        while guess in guessed_numbers:
            guess = random.randint(low, high)

        guessed_numbers.add(guess)
        attempts += 1

        print(f"My guess is: {guess}")
        feedback = input("Is it (h)igh, (l)ow, or (c)orrect? ").lower()

        if feedback == 'c':
            print(f"Yay! I guessed your number {guess} in {attempts} attempts!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input. Please enter 'h' for high, 'l' for low, or 'c' for correct.")

        # Check if the range is valid
        if low > high:
            print("Hmm, something doesn't add up. Are you sure about your hints?")
            break

if __name__ == "__main__":
    computer_guess_game()
