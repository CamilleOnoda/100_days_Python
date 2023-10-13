from machine_requirements import resources, MENU


def main():
    turn_off = False
    
    while not turn_off:
        order = input("What would you like? (espresso/latte/cappuccino): " )
        for resource, amount in resources.items():
            if resource in ["water", "milk"]:
                print(f"{resource.capitalize()}: {amount}ml")
            elif resource == "coffee":
                print(f"{resource.capitalize()}: {amount}g")
            elif resource == "money":
                print(f"{resource}: {amount}$")
            








if __name__ == "__main__":
    main()
