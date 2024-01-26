from random import randint
from art import logo

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_attempts(difficulty):
    """Returns number of attempts based on the selected difficulty."""
    if difficulty == "easy":
        return EASY_LEVEL_ATTEMPTS
    elif difficulty == "hard":
        return HARD_LEVEL_ATTEMPTS

def check_answer(guess, answer, attempts):
    """Checks if guess equals to answer and prints a result. Returns an actual number of attempts."""
    if guess == answer:
        print(f"You got it! The answer was {answer}.")
        return attempts-1
    elif guess > answer:
        print("Too high.")
        return attempts-1
    elif guess < answer:
        print("Too low.")
        return attempts-1

def play_game():
    """Plays a guessing game."""
    # Display welcome message.
    print(logo)
    print("Welcome to the Number Guessing Game!")

    # Set answer as a random number between 1 and 100.
    answer = randint(1, 100)
    print("I'm thinking of a number between 1 and 100.")

    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = set_attempts(difficulty)

    guess = 0
    # Attempt until the user guessed and has no attempts left.
    while guess != answer and attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        attempts = check_answer(guess, answer, attempts)

        if attempts > 0:
            print("Guess again.")
        elif attempts == 0:
            print("You've run out of guesses.")

while input("Do you want to play the Guessing Game? Type 'y' or 'n': ") == "y":
    play_game()
