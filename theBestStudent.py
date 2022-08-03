def createStudent(name: str, math: float, spanish: float, scients: float, literature: float, art: float) -> dict:
    student = {
        "nombre": name,
        "matematicas": math,
        "español": spanish,
        "ciencias": scients,
        "literatura": literature,
        "arte": art
    }
    return student


student1 = createStudent("Jose", 3.1, 0.1, 4, 5, 1)
student2 = createStudent("Pedro", 4, 2.3, 5, 2.2, 3.4)
student3 = createStudent("Carlos", 3.1, 0.1, 4, 5, 1)
student4 = createStudent("Maria", 5, 3.5, 4.2, 5, 3)
student5 = createStudent("Alex", 5, 3.5, 4.2, 5, 3)


def calculateAverage(math: float, spanish: float, scients: float, literature: float, art: float) -> float:
    return (math + spanish + scients + literature + art)/5


def theBestOfTheClassRoom(student1: dict, student2: dict, student3: dict, student4: dict, student5: dict) -> str:
    bestStudent = student1['nombre'].lower()
    bestAverage = calculateAverage(
        student1['matematicas'], student1['español'], student1['ciencias'], student1['literatura'], student1['arte'])
    averageStudent2 = calculateAverage(
        student2['matematicas'], student2['español'], student2['ciencias'], student2['literatura'], student2['arte'])
    averageStudent3 = calculateAverage(
        student3['matematicas'], student3['español'], student3['ciencias'], student3['literatura'], student3['arte'])
    averageStudent4 = calculateAverage(
        student4['matematicas'], student4['español'], student4['ciencias'], student4['literatura'], student4['arte'])
    averageStudent5 = calculateAverage(
        student5['matematicas'], student5['español'], student5['ciencias'], student5['literatura'], student5['arte'])
    if(averageStudent2 > bestAverage or (averageStudent2 == bestAverage and student2['nombre'].lower() < bestStudent)):
        bestAverage = averageStudent2
        bestStudent = student2['nombre'].lower()
    if(averageStudent3 > bestAverage or (averageStudent3 == bestAverage and student3['nombre'].lower() < bestStudent)):
        bestAverage = averageStudent3
        bestStudent = student3['nombre'].lower()
    if(averageStudent4 > bestAverage or (averageStudent4 == bestAverage and student4['nombre'].lower() < bestStudent)):
        bestAverage = averageStudent4
        bestStudent = student4['nombre'].lower()
    if(averageStudent5 > bestAverage or (averageStudent5 == bestAverage and student5['nombre'].lower() < bestStudent)):
        bestAverage = averageStudent5
        bestStudent = student5['nombre'].lower()

    return bestStudent


print(theBestOfTheClassRoom(student1, student2, student3, student4, student5))

# 3.74 3.54 3.56 3.62 3.98
