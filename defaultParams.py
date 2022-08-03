def elevateToXToY(x: int = 0, y: int = 0) -> int:
    return x**y


print(elevateToXToY(2))


def advanceSemestry(student1: dict = None, student2: dict = None, student3: dict = None, student4: dict = None) -> None:
    if (student1 != None):
        student1['ssc'] += 1
    if (student2 != None):
        student2['ssc'] += 1
    if (student3 != None):
        student3['ssc'] += 1
    if (student4 != None):
        student4['ssc'] += 1
