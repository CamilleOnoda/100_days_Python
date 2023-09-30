import random


stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ["rubicon", "starfield", "terminator", "hokkaido"]

# Generate a random word from the list
rand_word = random.choice(words)
word_length = len(rand_word)


# Generate as many blanks as letters in word
display = []
for _ in range(word_length):
    display += "_"


# Initiate the game
game_over = False
life = 6
while not game_over:
    print("Welcome to the Hangman game!\n")
    guess = input("\nChoose a letter: ").lower()

    if guess in display:
        print(f"You've already guessed the letter {guess}!")

    # If letter in word = replace the blank with the letter
    for position in range(word_length):
        letter = rand_word[position]
        if letter == guess:
            display[position] = guess


    # If letter not in word = lose a life
    # If the user run out of life = Game Over. Game stops
    if guess not in rand_word:
        print(f"You've guess the letter {guess}, this is not in the word! You lose a life!")
        life -= 1
        if life == 0:
            game_over = True
            print("Game Over!")
            print(f"The word was {rand_word}")


    # If all the blanks are filled, the user wins and the game stops
    if "_" not in display:
        game_over = True
        print("You won!")

    
    # Convert the list to a string
    print(f"{''.join(display)}")


    # Print the hangman image corresponding to the current number of lives
    print(stages[life])
