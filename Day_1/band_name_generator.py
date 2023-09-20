# Create a greeting
# Ask the user for the city they grew up in
# Ask the user for the name of a pet
# Combine the name of the city and the name of the pet and show their band name


print("Welcome to the band name generator!")
city = input("Where did you grow up in?\n")
pet = input("What is the name of your pet?\n")
band_name = city + " " + pet
print(f"Your band could be: {band_name}")
