# Write a program that calculates the average student height from a List of heights.
# You should not use the sum() or len() functions in your answer.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])


total_height = 0
total_number = 0
for height in student_heights:
  total_height += height
  total_number += 1

average = round(total_height / total_number)
print(average)
