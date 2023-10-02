"""def greet():
  name = input("Hi! What's your name?\n")
  print(f"Hello {name.title()}!")
  print("What a nice weather today!")
  print("Hope you're having a great day :)\n")


greet()"""

# Parameter = name
def greet_with(name, location):
    print(f"Hello {name.capitalize()}")
    print(f"How do you do {name.capitalize()}?")
    print(f"How is it like in {location.capitalize()}?")

# Argument = Camille
greet_with(location='nagoya', name="Camille")
