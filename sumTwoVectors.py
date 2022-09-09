def sum_tuples(vector1: tuple, vector2: tuple) -> tuple:
    vectorList = []
    for i in range(0, len(vector1)):
        vectorList.append(vector1[i] + vector2[i])

    return (vectorList[0], vectorList[1], vectorList[2])


vector1 = 2.3, 1.2, 3.9

vector2 = 1.2, 3, 8.9

print(sum_tuples(vector1, vector2))
