from art import logo
from random import randint
import time

print(logo)

def main():
    print("Let's begin...")
    print("I'm going to pick a number between 1 and 100.")
    time.sleep(2)
    print("Picking a number...")
    time.sleep(2)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while level not in ['easy', 'hard']:
        print("You must type 'easy' or 'hard'.")
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    play_game(level)


def play_game(level):
    correct_number = randint(1, 100)
    max_attemps = {'easy': 10, 'hard': 5}
    attempts = max_attemps[level]
    player_guess = []


    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess in player_guess:
            print("You've already used this number! Choose another one.")
            continue

        player_guess.append(guess)
        attempts -= 1

        if guess == correct_number:
            print(f"You win! You guessed the correct number: {correct_number}.")
            break
        elif guess > correct_number:
            print("Too high!")
        else:
            print("Too low!")

        if attempts == 0:
            print(f"You lose! The correct number was: {correct_number}!")
            break


if __name__ == "__main__":
    main()