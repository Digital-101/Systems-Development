employees = {'John':5000, 'Toby':7000, 'Happy':6000, 'Emily':5500}

students = {'Digit':'A',
            'Dylan':'A',
            'Wandisa':'B',
            'Andiswa': 'B',
            'Suraksha':'C',
            'Jongo':'B',
            'Thug':'D'}

def view_salary():
    name = input('Enter your name: ')
    if name in employees:
        message = (f'{name} is found and the salary is {employees.get(name)}')
    else:
        message = ('Employee is not found')
    return message

def get_grade():
    name = input('Enter your name: ')
    if name in students:
        message = (f'{name} is found and your grade is {students.get(name)}')
    else:
        message = ('Student is not found')
    return message

def get_name():
    grade = input('Enter your Grade: ')
    for n in students.items():
        if grade in n:
            return n[0]
    
print(view_salary())
print(get_grade())
print(get_name())
