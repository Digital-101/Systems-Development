students = {'Digit':25,
            'Dylan':21,
            'Wandisa':27,
            'Andiswa': 18,
            'Suraksha':18,
            'Jongo':21,
            'Thug':29}

#1 get
dvd = students.get('Digit')
print(dvd)

#2 pop
out = students.pop('Thug')

#3 keys
view = students.keys()
print(view)

#4 values
ages = students.values()
print(ages)

#5 items
for key, val in students.items():
    print(f'{key}: {val}')

#6 update
new = students.update({'Teen':17})
print(students)

#7 clear
empty = students.clear()
print(empty)