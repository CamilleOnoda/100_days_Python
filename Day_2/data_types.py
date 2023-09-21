 # Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8


two_digit_number = input("Type a two digit number: ")

split_convert_1 = int(two_digit_number[0])
split_convert_2 = int(two_digit_number[1])

add = split_convert_1 + split_convert_2

print(add)
