numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [nb ** 2 for nb in numbers]
print(squared_numbers)



list_of_strings = input().split(',')

# TODO: Use list comprehension to convert the strings to integers 👇:
list_integers = [int(x) for x in list_of_strings]

# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"
result = [nb for nb in list_integers if nb%2==0]

# Write your code 👆 above:
print(result)



