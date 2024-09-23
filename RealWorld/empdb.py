import mysql.connector

conn = mysql.connector.connect(
     user='admin', 
    host= 'localhost',
    password = 'Incorrect@24',
    database = 'cbi'
)

c = conn.cursor()
#c.execute('CREATE TABLE EMPLOYEES if not exist(employee_id INT AUTO_INCREMENT PRIMARY KEY, FIRSTNAME VARCHAR(20) NOT NULL, SURNAME VARCHAR(20) NOT NULL, SALARY DECIMAL(7,2) NOT NULL)')
#c.execute(q)
conn.commit()

def add_employee(first_name, surname, salary):
    query = 'INSERT INTO EMPLOYEES(FIRSTNAME, SURNAME, SALARY) VALUES (%s, %s, %s)'
    c.execute(query, (first_name, surname, salary))
    conn.commit()
    print('Employee has been added Successfully')

def view_employees():
    query = "SELECT * FROM EMPLOYEES"
    c.execute(query)
    result = c.fetchall()
    conn.commit()
    print('Employee details')
    for row in result:
        print(f'employee_id: {row[0]}, first_name: {row[1]}, surname: {row[2]}, salary: {row[3]}')

def update_employee(employee_id, firstname=None, surname=None, salary=None):
    if firstname:
        query = "update employees set firstname = %s where employee_id = %s"
        c.execute(query, (firstname, employee_id))

    if surname:
        query = "update employees set surname = %s where employee_id = %s"
        c.execute(query, (surname, employee_id))

    if salary:
        query = "update employees set salary = %s where employee_id = %s"
        c.execute(query, (salary, employee_id))
    conn.commit()
    print('Employee Updated Successfully')

def delete_employee(employee_id):
    if employee_id:
        query = 'delete from employees where employee_id = %s'
        c.execute(query, [employee_id])
    conn.commit()
    print('Employee Deleted Successfully')

#print(add_employee('Thug','Hooligan',900))
#print(update_employee(1, salary=5000))
print(delete_employee(2))
print(view_employees())

try:
    choice = int(input('---Enter your choice:--- \n1.ADD EMPLOYEE \n2.VIEW EMPLOYEES \n3.UPDATE EMPLOYEES \n4.DELETE EMPLOYEE\n'))
    if choice == 1:
        fname  = input('Enter employee firstname: ')
        lname  = input('Enter employee lastname: ')
        salary  = float(input('Enter employee salary: '))
        add_employee(fname,lname,salary)
    elif choice == 2:
        view_employees()
    elif choice == 3:
        update = int(input('==Choose value to update==: \n1.FIRSTNAME \n2.LASTNAME \n3.SALARY\n'))
        if update == 1:
            fname  = input('Enter employee firstname: ')
            id = int(input('Enter employee ID: '))
            update_employee(id, fname)
        elif update == 2:
            lname  = input('Enter employee lastname: ')
            id = int(input('Enter employee ID: '))
            update_employee(id, lname)
        elif update == 3:
            salary  = float(input('Enter employee salary: '))
            id = int(input('Enter employee ID: '))
            update_employee(id, salary)
    elif choice == 4:
        empid = int(input('Enter employee ID: '))
        delete_employee(empid)
except ValueError:
    print('Invalid Choice')
