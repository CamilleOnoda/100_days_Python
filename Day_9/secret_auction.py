from art import logo
import os
import platform

clear_command = 'cls' if platform.system() == 'Windows' else 'clear'

print(logo)
print("Welcome to the Silent Auction")

bids = {}
bid_history = {}


def main():
    name = input("What is your name? ").title()
    bid_price = int(input("What is your bid? $"))
    add_new_bidder(name, bid_price)
    new_bidder()


def add_new_bidder(name, bid_price):
    bids[name] = bid_price


def new_bidder():
    other_users = input("Are there other users who want to bid? ").lower()
    if other_users == "yes":
        clear_console()
        main()
    else:
        find_max_bidder()


def find_max_bidder():
    if bids:
        max_bid_price = max(bids.values())
        # Create a list of bidder names for the bidders whose bid price matches the maximum bid price
        max_bidders = [name for name, price in bids.items() if price == max_bid_price]

        if len(max_bidders) == 1:
            max_bidder = max_bidders[0]
            max_price = max_bid_price
            print(f"The winner is {max_bidder} with ${max_price}.")         
        else:
            print("It's a tie! The following bidders have the highest bid:")
            for bidder in max_bidders:
                print(f"{bidder} with ${max_bid_price}")
            
            # Clear bids and allow bidders to bid again
            bids.clear()
            new_bidders = input("Would you like to continue with new bids? ").lower()
            if new_bidders == "yes":
                clear_console()
                main()
            else:
                print("Auction ended.")         
    else:
        print("No bids were entered.")

    
def clear_console():
    os.system(clear_command)

if __name__ == "__main__":
    main()
