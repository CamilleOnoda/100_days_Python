# Prime numbers are numbers greater than 1 that only have two factors, 1 and the number itself. 
# This means that a prime number is only divisible by 1 and itself.


def prime_checker(number):
    is_prime = True

    if number == 1:
        print("It's not a prime number.")

    elif number > 1:
        for i in range(2, number): # If the number can be cleanly divisible by any number other than itself then it is not a prime number
            if number % i == 0:
                is_prime = False
        if is_prime:
            print("It's a prime number.")
        else:
            print("It's not a prime number.")


n = int(input())
prime_checker(number=n)
