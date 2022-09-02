def get_row_average(class_room: list, row: int) -> float:
    row_average = 0
    student_quantity = 0
    total_notes = 0
    if (row - 1 < 0 or row - 1 > len(class_room[row-1])):
        row_average = -1
    else:
        for i in range(0, len(class_room[row-1])):
            if (class_room[row-1][i] > 0):
                student_quantity += 1
                total_notes += class_room[row-1][i]
    row_average = round(total_notes/student_quantity, 2)
    return row_average


class_room = [[20, 14, 15, 16], [10, 15, 10, 17],
              [15, 15, 0, 10], [13, 17, 10, 10], [13, 17, 0, 5]]

print(get_row_average(class_room, 5))
