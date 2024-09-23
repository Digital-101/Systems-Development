# Input list of tuples
grades = [
    ('Alice', 85),
    ('Bob', 78),
    ('Alice', 90),
    ('Bob', 82),
    ('Alice', 95)
]

# Initialize an empty dictionary to store cumulative grades and counts
grade_sums = {}
grade_counts = {}

# Process each tuple in the list
for name, grade in grades:
    if name in grade_sums:
        grade_sums[name] += grade
        grade_counts[name] += 1
    else:
        grade_sums[name] = grade
        grade_counts[name] = 1

# Calculate the average grades
average_grades = {name: (grade_sums[name] / grade_counts[name]) for name in grade_sums}

print(average_grades)
