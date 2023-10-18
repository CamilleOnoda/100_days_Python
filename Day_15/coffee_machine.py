from machine_requirements import resources, MENU, coins
from art import logo


def main():
    turn_off = False
    print(logo)

    while not turn_off:
        order = input("What would you like (espresso/latte/cappuccino)?\n"
                      "Enter 'report' to see the current resources, or 'off' to stop the machine: ").lower()

        if order == 'off':
            turn_off = True

        if order == 'report':
            for resource, amount in resources.items():
                if resource in ["water", "milk"]:
                    print(f"{resource.capitalize()}: {amount}ml")
                elif resource == "coffee":
                    print(f"{resource.capitalize()}: {amount}g")
                elif resource == "money":
                    print(f"{resource.capitalize()}: {amount}$")

        elif order in {"espresso", "latte", "cappuccino"}:
            #payment(order)
            prepare_order(order)
            

def prepare_order(drink_type):
    ingredients = MENU[drink_type]["ingredients"]
    
    for ingredient, amount in ingredients.items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is enough {ingredient}.")
            return
        else:
            resources[ingredient] -= amount
    
    payment(drink_type)
    resources["money"] += drink_cost
    print(f"Here is your {drink_type}. Enjoy!☕\n")


def payment(drink_type):
    global drink_cost
    drink_cost = MENU[drink_type]["cost"]
    amount_paid = 0
    
    print(f"Amount due: ${round(drink_cost - amount_paid, 2)}")

    while amount_paid < drink_cost:
        #print(f"Amount due: ${round(drink_cost - amount_paid, 2)}")
        for coin, value in coins.items():
            coin_inserted = int(input(f"How many {coin}? "))
            total = coin_inserted * value
            amount_paid += total
            amount_left = drink_cost - amount_paid

            if amount_paid == drink_cost:
                return
            elif amount_paid > drink_cost:
                change_owed = amount_paid - drink_cost
                print(f"Your change: ${round(change_owed, 2)}")
                return
            else:
                print(f"Amount due: ${round(amount_left, 2)}")
            
        if amount_paid == drink_cost:
            return
        
        return drink_cost


if __name__ == "__main__":
    main()
