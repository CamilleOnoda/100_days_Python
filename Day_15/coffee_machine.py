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
            







if __name__ == "__main__":
    main()