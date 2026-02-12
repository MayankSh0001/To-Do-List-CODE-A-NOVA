import random

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")
    print("I will choose a number and you have to guess it.")

    # Difficulty levels
    print("\nSelect Difficulty Level:")
    print("1. Easy (1 to 50, 10 attempts)")
    print("2. Medium (1 to 100, 7 attempts)")
    print("3. Hard (1 to 200, 5 attempts)")

    choice = int(input("Enter your choice (1/2/3): "))

    if choice == 1:
        max_number = 50
        attempts = 10
    elif choice == 2:
        max_number = 100
        attempts = 7
    elif choice == 3:
        max_number = 200
        attempts = 5
    else:
        print("Invalid choice! Defaulting to Medium level.")
        max_number = 100
        attempts = 7

    secret_number = random.randint(1, max_number)

    print(f"\nI have selected a number between 1 and {max_number}.")
    print(f"You have {attempts} attempts to guess it.\n")

    for i in range(attempts):
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the number in {i+1} attempts.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
    else:
        print(f"\n❌ Sorry! You ran out of attempts. The number was {secret_number}.")

# Run the game
number_guessing_game()

# Ask if the player wants to play again
while True:
    play_again = input("\nDo you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        number_guessing_game()
    elif play_again.lower() == "no":
        print("Thanks for playing! Goodbye.")
        break