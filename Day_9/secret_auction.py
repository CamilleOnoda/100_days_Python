from art import logo
import os

print(logo)

bids = {}
def main():
    name = input("What is your name? ")
    bid_price = int(input("What is your bid? $"))
    add_new_bid(name, bid_price)
    new_bidder()


def add_new_bid(name, bid_price):
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
        # Telling Python to find the key (i.e., bidder's name) in the bids dictionary 
        # that corresponds to the maximum value (i.e., highest bid price).
        # .get() is used to retrieve the value associated with a given key in a dict.
        max_bidder = max(bids, key=bids.get)
        max_price = bids[max_bidder]
        print(f"The winner is {max_bidder} with ${max_price}.")
    else:
        print("No bids were entered.")

    
# To clear the console
def clear_console():
    os.system('cls')


if __name__ == "__main__":
    main()
