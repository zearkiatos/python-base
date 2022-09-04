def plus(number: int):
    return number + number


def minus(number: int):
    return number - number


def prod(number: int):
    return number * number


def division(number: int):
    return number / number


def reprint_x(matrix: list, operation: str) -> list:
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if (i == j or j == len(matrix) - 1 - i):
                if operation == "+":
                    matrix[i][j] = plus(matrix[i][j])
                if operation == "-":
                    matrix[i][j] = minus(matrix[i][j])
                if operation == "*":
                    matrix[i][j] = prod(matrix[i][j])
                if operation == "/":
                    matrix[i][j] = division(matrix[i][j])

    return matrix


matrix = [[1, 3], [9, 2]]

print(reprint_x(matrix, "+"))

matrix = [[1, 3], [9, 2]]

print(reprint_x(matrix, "-"))

matrix = [[1, 3], [9, 2]]

print(reprint_x(matrix, "*"))

matrix = [[1, 3], [9, 2]]

print(reprint_x(matrix, "/"))
