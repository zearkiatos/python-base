
def get_homework_stats_calculator(students_homeworks: dict, homework: str) -> dict:
    stats = {}
    major_note = 0
    student_with_major_note = ''
    worse_note = 1000
    worse = ''
    average = 0
    count_student_completed_homework = 0
    total_notes = 0
    for student in students_homeworks:
        if (list(students_homeworks[student]).count(homework)):
            count_student_completed_homework+=1
            total_notes += students_homeworks[student][homework] 
            if(students_homeworks[student][homework] > major_note):
                major_note = students_homeworks[student][homework]
                student_with_major_note = student
            if(students_homeworks[student][homework] < worse_note):
                worse_note = students_homeworks[student][homework]
                worse = student
    if count_student_completed_homework:
        average = total_notes/count_student_completed_homework
    stats['major'] = major_note
    stats['best'] = student_with_major_note
    stats['minor'] = worse_note
    stats['worse'] = worse
    stats['average'] = average
    stats['quantity'] = count_student_completed_homework
    stats['total'] = total_notes
    return stats


homeworks = {
    "Roberto": {
        # "Tarea1": 80,
        "Tarea2": 90
    },
    "Pedro": {
        # "Tarea1": 10,
        "Tarea2": 20,
        "Tarea3": 20
    },
    "Maria": {
        # "Tarea1": 60,
        "Tarea2": 80,
        "Tarea3": 90
    }
}

print(get_homework_stats_calculator(homeworks, 'Tarea1'))
