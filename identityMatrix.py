


def get_identity_matrix(n:int)->list:
    matrix = []
    for i in range(0, n):
        matrix.append([0]*n)
    for i in range(0, n):
        for j in range(0, n):
            matrix[i][j] = 0
        matrix[i][i] = 1
    return matrix

def main_identity_matrix()->None:
    n = int(input("Type a number of column and field "))
    matrix = get_identity_matrix(n)

    print(matrix)

main_identity_matrix()