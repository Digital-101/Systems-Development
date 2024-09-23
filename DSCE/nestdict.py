students = {'Digit':{'English':80, 'Maths':78},
            'Wandisa': {'English':90, 'Maths':78},
            'Andiswa': {'English':87, 'Maths':88}}

def get_ov_grade():
    name = input('Enter student name: ')
    msg = ''
    if name in students:
        msg = f'{name} found and overall grade is: {students.get(name)}'
    else:
        msg = f'{name} not Found'
    return msg

def get_stud_grade():
    output = {}
    subject = input('Enter your subject: ')
    for k, v in students.items():
        if subject in v:
            output[k] = v[subject]
    return output

def get_stud_subj():
    grade = int(input('Enter your grade: '))
    results = []  
    for k, v in students.items():
        if grade in v.values():
            results.append(k)
    return results

def get_grade():
    name = input('Enter student name: ')
    subject = input('Enter your subject: ')
    if name in students:
        if subject in students[name]:
            return students[name][subject]
        return f"Subject '{subject}' not found for student '{name}'."
    else:
        return f"Student '{name}' not found."

#print(get_ov_grade())
#print(get_stud_grade())
#print(get_stud_subj())
print(get_grade())