"""You are going to write a program that tests the compatibility between two people.

To work out the love score between two people:

Take both people's names and check for the number of times the letters in the word TRUE occurs. 

Then check for the number of times the letters in the word LOVE occurs. 

Then combine these numbers to make a 2 digit number."""

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]
true_count = 0
love_count = 0

for letter in name1:
    if letter in true:
        true_count += 1
    if letter in love:
        love_count += 1

for letter in name2:
    if letter in true:
        true_count += 1
    if letter in love:
        love_count += 1

total = f"{true_count}{love_count}"
total = int(total)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif 40 <= total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")

