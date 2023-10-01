# Round up a number = ceil() function
# The ceil() function gets its name from the mathematical term ceiling, 
# which describes the nearest integer that's greater than or equal to a given number.

from math import ceil


def paint_calc(height, width, cover):
    number_cans = (height * width) / cover
    round_up = ceil(number_cans)
    print(f"You'll need {round_up} cans of paint.")
    


test_h = int(input()) # height of wall (m)
test_w = int(input()) # width of wall (m)
coverage = 5

paint_calc(height=test_h, width=test_w, cover=coverage)
