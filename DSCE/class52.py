students = {'Andiswa':{'Maths':88, 'LO':74, 'English':65}, 
            'Wandisa':{'Accounting':78, 'LO':58, 'English':69}, 
            'Jongo':{'Life Science':76, 'LO':74, 'English':58},
            'Mthunzi':{'Business':92, 'LO':90, 'English':85}}

def get_overallGrade():
    s_name = input('Enter student name: ')
    msg = ''
    if s_name in students:
        msg = f'{s_name} found and overall grade is: {students.get(s_name)}'
    else:
        msg = f'{s_name} is not found'
    return msg

def get_names_grades():
    subject = input('Enter your subject: ')
    results = dict()
    for student, subjects in students.items():
        if subject in subjects:
            results[student] = subjects[subject]
    return results

def get_names_subject():
    grade = int(input('Enter your grade: '))
    results = []
    for student, subjects in students.items():
        if grade in subjects.values():
            results.append(student)
    return results   

def get_grade_subject():
    name = input('Enter student name: ')    
    subject = input('Enter subject: ')   
    if name in students:
        if subject in students[name]:
            return students[name][subject]
        else:
            return f"Subject '{subject}' not found for student '{name}'."
    else:
        return f"Student '{name}' not found."
    
#print(get_overallGrade())
print(get_names_grades())
#print(get_names_subject())
#print(get_grade_subject())