def sum_all_values(matrix: list) -> int:
    total = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            total += matrix[i][j]

    return total


def sum_of_especify_row(matrix: list, row: int) -> int:
    total = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if (i + 1 == row):
                total += matrix[i][j]
    return total


def sum_of_especify_column(matrix: list, column: int) -> int:
    total = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if (j + 1 == column):
                total += matrix[i][j]
    return total


def is_there_some_nagative_value(matrix: list) -> bool:
    there_is_negative = False
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            if (matrix[i][j] < 0):
                there_is_negative = True
                break
    return there_is_negative


def row_with_more_zeros(matrix: list) -> int:
    row_with_more_zero = 0
    zeros_by_rows = [0]*len(matrix)
    grantest_zeros_quantity = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if (matrix[i][j] == 0):
                zeros_by_rows[i] += 1

    for i in range(0, len(zeros_by_rows)):
        if(zeros_by_rows[i] > grantest_zeros_quantity):
            row_with_more_zero = i + 1
            grantest_zeros_quantity = zeros_by_rows[i]

    return row_with_more_zero


matrix = [[1, 2], [4, 2]]

matrix2 = [[1, -2], [4, 2]]

matrix3 = [[1, 2, 5], [4, 0, 0], [1, -2, 1], [0, 0, 0]]

print(sum_all_values(matrix))

print(sum_of_especify_row(matrix, 1))

print(sum_of_especify_column(matrix, 2))

print(is_there_some_nagative_value(matrix2))

print(row_with_more_zeros(matrix3))
