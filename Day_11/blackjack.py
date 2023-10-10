import random
import os
from art import logo


def play_blackjack():
    clear_console()
    print(logo)

    while True:
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        user_hand = []
        computer_hand = []

        for _ in range(2):
            deal_card(cards, user_hand)
            deal_card(cards, computer_hand)

        user_score = calculate_score(user_hand)
        computer_score = calculate_score(computer_hand)

        print(f"    Your cards: {user_hand}, current score: {user_score}")
        print(f"    Computer's first card: {computer_hand[0]}")

        if user_score == 21 and len(user_hand) == 2:
            print("BlackJack! You win!")
        elif computer_score == 21 and len(computer_hand) == 2:
            print("BlackJack! Computer wins!")
        else:
            while user_score < 21:
                user_choice = input("Type 'y' to get another card, 'n' to pass: ")
                if user_choice == 'y':
                    deal_card(cards, user_hand)
                    user_score = calculate_score(user_hand)
                    print(f"    Your cards: {user_hand}, current score: {user_score}")
                else:
                    break

            while computer_score < 17:
                deal_card(cards, computer_hand)
                computer_score = calculate_score(computer_hand)

            print(f"    Your final hand: {user_hand}, final score: {user_score}")
            print(f"    Computer's final hand: {computer_hand}, final score: {computer_score}")

            if user_score > 21:
                print("You went over. Computer wins.")
            elif computer_score > 21:
                print("Computer went over. You win.")
            elif user_score > computer_score:
                print("You win!")
            elif computer_score > user_score:
                print("Computer wins.")
            else:
                print("It's a tie!")

        play_again = input("Do you want to play again? Type 'y' for yes, 'n' for no: ")
        if play_again != 'y':
            break
        else:
            clear_console()


def deal_card(deck, hand):
    card = random.choice(deck)
    hand.append(card)


def calculate_score(hand):
    score = sum(hand)
    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
    return score


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    play_blackjack()
