students = [
    {'name':'john','score':90},
    {'name':'bob','score':85},
    {'name':'alice','score':78},
    {'name':'charlie','score':92},
    ]

avg_score = sum(student['score'] for student in students) / len(students)

grades = []

for student in students:
    if student['score'] >= 90:
        grade = 'A'
    elif student['score'] >= 80:
        grade = 'B'
    elif student['score'] >= 70:
        grade = 'C'
    elif student['score'] >= 60:
        grade = 'D'
    elif student['score'] >= 50:
        grade = 'E'
    else:
        grade = 'F'
    grades.append((student['score'], grade))

print('Average score: ',avg_score)
for name, grade in grades:
    print(f'{name}: {grade}')

if avg_score > 80:
    print('Congratulations! The average score is above 80!')