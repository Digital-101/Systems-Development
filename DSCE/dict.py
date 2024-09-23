# Dictionary containing student data
students = {
    'Andiswa': {'Maths': 88, 'LO': 73, 'English': 65},
    'Wandisa': {'Accounting': 78, 'LO': 58, 'English': 69},
    'Jongo': {'Life Science': 76, 'LO': 74, 'English': 58},
    'Mthunzi': {'Business': 92, 'LO': 90, 'English': 85}
}

def get_students_by_subject(subject):
    """
    Returns a dictionary of student names and grades for a given subject.
    
    Args:
    - subject (str): The subject to search for.
    
    Returns:
    - dict: A dictionary of student names and their grades for the subject.
    """
    results = {}
    for student, subjects in students.items():
        if subject in subjects:
            results[student] = subjects[subject]
    return results

def get_students_by_grade(target_grade):
    """
    Returns a list of student names who have a specific grade in any subject.
    
    Args:
    - target_grade (int): The grade to search for.
    
    Returns:
    - list: A list of student names who have the target grade.
    """
    results = []
    for student, subjects in students.items():
        if target_grade in subjects.values():
            results.append(student)
    return results

def get_grade(student_name, subject):
    """
    Returns the grade of a specific student for a given subject.
    
    Args:
    - student_name (str): The name of the student.
    - subject (str): The subject to search for.
    
    Returns:
    - int or str: The grade for the subject, or an error message if not found.
    """
    if student_name in students:
        if subject in students[student_name]:
            return students[student_name][subject]
        else:
            return f"Subject '{subject}' not found for student '{student_name}'."
    else:
        return f"Student '{student_name}' not found."

# Example usage
if __name__ == "__main__":
    # Testing get_students_by_subject
    print("Students with grades in 'English':")
    print(get_students_by_subject('English'))
    
    # Testing get_students_by_grade
    print("\nStudents with grade 58:")
    print(get_students_by_grade(58))
    
    # Testing get_grade
    print("\nGrade for 'Andiswa' in 'Maths':")
    print(get_grade('Andiswa', 'Maths'))
    
    print("\nGrade for 'Wandisa' in 'Science':")
    print(get_grade('Wandisa', 'Science'))
    
    print("\nGrade for 'Nonexistent' in 'Maths':")
    print(get_grade('Nonexistent', 'Maths'))
    
    print("\nGrade for 'Jongo' in 'LO':")
    print(get_grade('Jongo', 'LO'))
