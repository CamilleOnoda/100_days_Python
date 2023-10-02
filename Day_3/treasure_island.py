print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

left_right = input("You're at a cross road. Where do you want to go?"
                   f"Type 'left' or 'right': ").lower()

if left_right != "left":
    print("Game over! You fell into a hole!")
elif left_right == "left":
    wait_swim = input("You come to a lake. There is an island in the middle of the lake."
                      f"Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if wait_swim != "swim":
        print("Attacked by a trout! Game over!")
    elif wait_swim == "wait":
        color = input("You arrive at the island unharmed. There is a house with 3 doors."
              f"One red, one yellow and one blue. Which colour do you choose? ").lower()
        if color == "red":
            print("Burned by fire! Game over!")
        elif color == "yellow":
            print("You win!!")
        else:
            print("Game over!!")

