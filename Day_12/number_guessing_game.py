from art import logo
from random import randint
import time

print(logo)

def main():
    global level

    print("Let's begin...")
    print("I'm going to pick a number between 1 and 100.")
    time.sleep(2)
    print("Picking a number...")
    time.sleep(2)

    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    while level not in ['easy', 'hard']:
        print("You must type 'easy' or 'hard'.")
        level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    play_game()


def play_game():
    correct_number = randint(1, 100)
    max_attemps = {'easy': 10, 'hard': 5}
    attempts = max_attemps[level]
    easy_level = 10
    hard_level = 5
    player_guess = []
    player_attempt = 0

    if level == 'easy':
        print(f"You have {easy_level} attempts remaining to guess the number.")
    elif level == 'hard':
        print(f"You have {hard_level} attempts remaining to guess the number.")
        
    while player_guess != correct_number:
        guess = int(input("Make a guess: "))
        if guess in player_guess:
            print("You've already used this number! Choose another one.")
        elif guess == correct_number:
            print(f"You win! You guessed the correct number: {correct_number}.")
            break
        else:
            player_guess.append(guess)
            player_attempt += 1

            if level == 'easy':
                attempts = easy_level - player_attempt
                if attempts == 0:
                    print(f"You lose. The correct number was: {correct_number}.")
                    break
                else:
                    print(f"You have {attempts} attempts remaining to guess the number.")

            elif level == 'hard':
                attempts = hard_level - player_attempt
                if attempts == 0:
                    print(f"You lose. The correct number was: {correct_number}.")
                    break
                else:
                    print(f"You have {attempts} attempts remaining to guess the number.")

        if guess > correct_number:
            print("Too high!")
        elif guess < correct_number:
            print("Too low!")


if __name__ == "__main__":
    main()
