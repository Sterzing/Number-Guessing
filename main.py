# "Welcome to the Number Guessing Game!"
# "I'm thinking of a number between 1 and 100."
# "Choose a difficulty. Type 'easy' or 'hard': "
# "You have {attempts_remaing} attempts remaining to guess the number"
# "Make a guess: "
# "Too High"
# "Guess Again"
# "You got it! The answer was {MAGIC_NUMBER}"
# "You've run out of guesses. You lose!"

from art import logo
import random
MAGIC_NUMBER = random.randint(1, 100)
is_game_over = False
user_guess = 0
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")


def choose_level(level):
    if level == "easy":
        attempts_remaining = 10
    else:
        attempts_remaining = 5
    return attempts_remaining

attempts_remaining = choose_level(input("Choose a difficulty. Type 'easy' or 'hard': ").lower())

def check_guess(guess):
    if user_guess == MAGIC_NUMBER:
        return f"You got it! The answer was {MAGIC_NUMBER}"
    if user_guess > MAGIC_NUMBER:
        return"Too High"
    elif user_guess < MAGIC_NUMBER:
        return  "Too low"

while user_guess != MAGIC_NUMBER and is_game_over == False:
    print(f"You have {attempts_remaining} attempts remaining to guess the number")
    attempts_remaining -= 1
    user_guess = int(input("Make a guess: "))
    print(check_guess(user_guess))
    if attempts_remaining == 0:
        print("You've run out of guesses. You lose!")
        is_game_over = True
    elif user_guess == MAGIC_NUMBER:
        is_game_over = True
    else:
        print("Guess again")











