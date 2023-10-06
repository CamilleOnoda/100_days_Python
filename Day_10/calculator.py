from art import logo
import os
import platform

clear_command = 'cls' if platform.system() == 'Windows' else 'clear'

print(logo)


def main():
    end_calculator = False
    result = 0
    
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
                try:
                    result = function(num1, num2)
                    print(result)
                except ZeroDivisionError as e:
                    result = str(e)
                    print(result)
                    break
        
        # 'isinstance' is a built-in function that is used to check the type of an object. 
        # If 'result' is a string, this condition will evaluate to True.
        if isinstance(result, str) and "Division by zero is not allowed" in result:
            continue_calc = input(f"Type 'n' to restart a new calculation,"
                                " or type 'end' to end the program: ")
        else:
            continue_calc = input(f"Type 'y' to continue calculating with {result}, "
                             "type 'n' to restart a new calculation,"
                             " or type 'end' to end the program: ")
    
        if continue_calc == "y":
            clear_console()
        elif continue_calc == "n":
            clear_console()
            result = 0
        elif continue_calc == "end":
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
    if n2 == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return n1 / n2
    

def exponent(n1, n2):
    return n1 ** n2


def clear_console():
    os.system(clear_command)


if __name__ == "__main__":
    main()
