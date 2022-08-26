

def definity_calculation(students: list) -> list:
    student_final_grade = students.copy()
    for student in student_final_grade:
        if (student['nota'] >= 4.5):
            student['nota'] = 5.0
        elif (student['nota'] >= 3.5 and student['nota'] < 4.5):
            student['nota'] = 4.0
        elif (student['nota'] >= 2.5 and student['nota'] < 3.5):
            student['nota'] = 3.0
        else:
            student['nota'] = 1.5
    return student_final_grade


students = [{
    'nombre': 'Pedro',
    'nota': 4.5
},
    {
    'nombre': 'Maria',
    'nota': 3.5
},
    {
    'nombre': 'Luis',
    'nota': 2.7
},
    {
    'nombre': 'Carla',
    'nota': 1
}]

print(definity_calculation(students))
