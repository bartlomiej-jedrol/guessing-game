import random
from art import logo

def guessing_game():
    """Play a guessing game"""
    print(logo)
    print("Welcome to the Number Guessing Game!")

    # Get random number between 1 and 100.
    random_number = random.randint(1, 100)
    print("I'm thinking of a number between 1 and 100")

    # Determine difficulty.
    attempts_left = 0
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts_left = 10
    elif difficulty == "hard":
        attempts_left = 5
    else:
        attempts_left = 0

    is_guessed = False
    # Check if guessed until the user has the attempts left. 
    while attempts_left > 0 and not is_guessed:
        print(f"You have {attempts_left} attempts remaining to guess the number.")
        attempts_left -= 1
        
        guess = int(input("Make a guess: "))
        if guess == random_number:
            is_guessed = True
            print(f"You got it! The answer was {random_number}.")
        elif guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low.")

        if is_guessed == False and attempts_left > 0:
            print("Guess again.")

        if is_guessed == False and attempts_left == 0:
            print("You've run out of guesses.")
        
while input("Do you want to play the Guessing Game? Type 'y' or 'n': ") == "y":
    guessing_game()