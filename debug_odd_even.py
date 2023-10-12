"""Incorrect code"""
number = int(input())

if number % 2 = 0: #SyntaxError
  print("This is an even number.")
else:
  print("This is an odd number.")


"""Correct code"""
number = int(input())

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")