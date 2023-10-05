from art import logo
import os


print(logo)


def main():
    result = 0
    end_calculator = False
    
    while not end_calculator:
        if result != 0:
            num1 = result
        else:
            num1 = float(input("What's the first number? "))

        operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
            "**": exponent,
        }
        
        for operation in operations:
            print(operation)

        pick_op = pick_operation()
  
        num2 = float(input("What's the second number? "))
        
        for operation, function in operations.items():
            if pick_op == operation:
                result = function(num1, num2)
                print(result)

        continue_calc = input(f"Type 'y' to continue calculating with {result}, "
                             "or type 'n' to restart a new calculation: ")
    
        if continue_calc == "y":
            clear_console()
        else:
            end_calculator = True
            print("See you next time!")


def pick_operation():
    pick_op = input("Pick an operation: ")
    return pick_op


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    try:
        n1 / n2
    except ZeroDivisionError:
        return "Division by zero is not allowed."
    

def exponent(n1, n2):
    return n1 ** n2


def clear_console():
    os.system('cls')


if __name__ == "__main__":
    main()
