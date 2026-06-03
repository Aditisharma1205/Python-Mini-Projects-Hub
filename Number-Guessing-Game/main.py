from art import logo
import random


def play_game():
    print(logo)
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)

    while True:
        level = input("\nChoose a difficulty (easy/difficult): ").lower()

        if level == "easy":
            attempts = 10
            break
        elif level == "difficult":
            attempts = 5
            break
        else:
            print("Invalid difficulty. Please enter 'easy' or 'difficult'.")

    guess_history = []

    while attempts > 0:
        print(f"\nAttempts remaining: {attempts}")

        try:
            user_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        guess_history.append(user_guess)

        if user_guess == secret_number:
            print(f"\nCongratulations! You guessed the number {secret_number}.")
            print(f"Total guesses: {len(guess_history)}")
            print(f"Your guesses: {guess_history}")
            return

        elif user_guess < secret_number:
            print("📉 Too low!")

        else:
            print("📈 Too high!")

        attempts -= 1

        if attempts > 0:
            print("🔄 Guess again!")

    print(f"\nGame Over! You ran out of attempts.")
    print(f"The number was: {secret_number}")
    print(f"Your guesses: {guess_history}")


while True:
    play_game()

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        break
