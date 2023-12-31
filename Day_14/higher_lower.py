from art import logo, logo_2
from game_data import data
import random
import os


def main():
    global score
    score = 0

    end_game = False

    print(logo)

    while not end_game:
        #print(logo)

        a, b = random_choice()

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear_console()

        end_game = compare(a, b, guess)
        

def random_choice():
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowel_str = ''.join(vowel)
    a = random.choice(data)
    b = random.choice(data)
    description_a = a['description']
    description_b = b['description']

    if 'United States' in a.values() and any(description_a.startswith(v) for v in vowel_str):
        print(f"Compare A: {a['name']}, an {a['description']}, from the {a['country']}.")

    elif 'United States' in a.values():
        print(f"Compare A: {a['name']}, a {a['description']}, from the {a['country']}.")

    elif any(description_a.startswith(v) for v in vowel_str):
        print(f"Compare A: {a['name']}, an {a['desgit scription']}, from {a['country']}.")

    else:
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}.")

    print(logo_2)

    if 'United States' in b.values() and any(description_b.startswith(v) for v in vowel_str):
        print(f"Against B: {b['name']}, an {b['description']}, from the {b['country']}.")

    elif 'United States' in b.values():
        print(f"Against B: {b['name']}, a {b['description']}, from the {b['country']}.")

    elif any(description_b.startswith(v) for v in vowel_str):
        print(f"Against B: {b['name']}, an {b['description']}, from {b['country']}.")

    else:
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}.")
    
    return a, b


def compare(a, b, guess):
    global score
    if a['follower_count'] > b['follower_count'] and guess == 'a':
        score += 1
        print(logo)
        print(f"You're right! Current score: {score}.")
        return False

    elif b['follower_count'] > a['follower_count'] and guess == 'b':
        score += 1
        print(logo)
        print(f"You're right! Current score: {score}.")
        return False
    else:
        print(logo)
        print(f"You're wrong! Final score: {score}.")
        return True


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()
