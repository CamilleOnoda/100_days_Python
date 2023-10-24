import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print()

# Loop through a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Lily":
        print(row.score)