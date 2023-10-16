from machine_requirements import resources, MENU


def main():
    turn_off = False

    while not turn_off:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

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
            
        if order == "espresso":
            espresso_amount_water = MENU["espresso"]["ingredients"]["water"]
            espresso_amount_coffee = MENU["espresso"]["ingredients"]["coffee"]

            if espresso_amount_water > resources["water"]:
                print("Sorry, there is not enough water.")
            elif espresso_amount_coffee > resources["coffee"]:
                print("Sorry, there is not enough coffee.")
            else:
                resources["water"] -= espresso_amount_water
                resources["coffee"] -= espresso_amount_coffee
                print(f"Water: {resources['water']}")
                print(f"Coffee: {resources['coffee']}")

        if order == "latte":
            latte_amount_water = MENU["latte"]["ingredients"]["water"]
            latte_amount_coffee = MENU["latte"]["ingredients"]["coffee"]
            latte_amount_milk = MENU["latte"]["ingredients"]["milk"]

            if latte_amount_water > resources["water"]:
                print("Sorry, there is not enough water.")
            elif latte_amount_coffee > resources["coffee"]:
                print("Sorry, there is not enough coffee.")
            elif latte_amount_milk > resources["milk"]:
                print("Sorry, there is not enough milk.")
            else:
                resources["water"] -= latte_amount_water
                resources["coffee"] -= latte_amount_coffee
                resources["milk"] -= latte_amount_milk
                print(f"Water: {resources['water']}")
                print(f"Coffee: {resources['coffee']}")
                print(f"Milk: {resources['milk']}")

        if order == "cappuccino":
            cappuccino_amount_water = MENU["cappuccino"]["ingredients"]["water"]
            cappuccino_amount_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
            cappuccino_amount_milk = MENU["cappuccino"]["ingredients"]["milk"]

            if cappuccino_amount_water > resources["water"]:
                print("Sorry, there is not enough water.")
            elif cappuccino_amount_coffee > resources["coffee"]:
                print("Sorry, there is not enough coffee.")
            elif cappuccino_amount_milk > resources["milk"]:
                print("Sorry, there is not enough milk.")
            else:
                resources["water"] -= cappuccino_amount_water
                resources["coffee"] -= cappuccino_amount_coffee
                resources["milk"] -= cappuccino_amount_milk
                print(f"Water: {resources['water']}")
                print(f"Coffee: {resources['coffee']}")
                print(f"Milk: {resources['milk']}")

            

if __name__ == "__main__":
    main()