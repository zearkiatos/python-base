BOTTLE = "BOTTLE"

CAKE = "CAKE"

BOTTLE_COST = 120000
CAKE_COST = 35000

THERE_ARE_COW = 'There is COW'

IT_IS_NOT_ENOUGH = 'It is not enough'


def make_cow(class_room: list, cow: str) -> list:
    position_of_student_row = 0
    position_of_student_column = 0
    grantest_colaboration = 0
    total_collection = 0
    list_result = []
    message = IT_IS_NOT_ENOUGH
    for i in range(0, len(class_room)):
        for j in range(0, len(class_room[i])):
            if (class_room[i][j] > grantest_colaboration):
                grantest_colaboration = class_room[i][j]
                position_of_student_row = i
                position_of_student_column = j
            total_collection += class_room[i][j]
    if (cow == BOTTLE and total_collection >= BOTTLE_COST):
        message = THERE_ARE_COW
    if (cow == CAKE and total_collection >= CAKE_COST):
        message = THERE_ARE_COW
    
    list_result.append(message)
    list_result.append(position_of_student_row)
    list_result.append(position_of_student_column)

    return list_result


class_room = [[20, 40, 50, 60], [100, 500, 1000, 70000],
              [5000, 7500, 10000, 100], [30000, 7500, 10000, 1000]]


print(make_cow(class_room, BOTTLE))
