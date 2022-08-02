def createStudent(name: str, code: str, genre: str, career: str, average: float, ssc: float, semestry: int) -> dict:
    student = {
        "name": name,
        "code": code,
        "genre": genre,
        "career": career,
        "average": average,
        "ssc": ssc,
        "semestry": semestry
    }
    return student


student1 = createStudent("Juan Pérez", "201824736",
                         "male", "Biology", 3.78, 0.7, 1)
student2 = createStudent("Ana Gavalda", "201724736",
                         "female", "Polic Scientics", 4.25, 3.5, 1)
student3 = createStudent("Bastien Bosa", "201815217",
                         "male", "Economic", 3.21, 2.3, 1)
student4 = createStudent("Catalina Gómez", "201715400",
                         "female", "Art", 3.8, 4, 1)


def searchStudent(student1: dict, student2: dict, student3: dict, student4: dict, search: str) -> dict:
    studentFound = None
    if(student1["name"] == search):
        studentFound = student1
    elif(student2["name"] == search):
        studentFound = student2
    elif(student3["name"] == search):
        studentFound = student3
    elif(student4["name"] == search):
        studentFound = student4
    return studentFound


def advanceSemestry(student1: dict, student2: dict, student3: dict, student4: dict) -> None:
    student1["semestry"] += 1
    student2["semestry"] += 1
    student3["semestry"] += 1
    student4["semestry"] += 1


def whoAreInRisk(student1: dict, student2: dict, student3: dict, student4: dict) -> dict:
    studentsWithRisk = {}
    if(student1["average"] < 3.4):
        studentsWithRisk = {
            student1["name"]: {
                "code": student1["code"],
                "average": student1["average"]
            }
        }
    if(student2["average"] < 3.4):
        studentsWithRisk = {
            student2["name"]: {
                "code": student2["code"],
                "average": student2["average"]
            }
        }
    if(student3["average"] < 3.4):
        studentsWithRisk = {
            student3["name"]: {
                "code": student3["code"],
                "average": student3["average"]
            }
        }
    if(student4["average"] < 3.4):
        studentsWithRisk = {
            student4["name"]: {
                "code": student4["code"],
                "average": student4["average"]
            }
        }

    return studentsWithRisk


def initialization() -> None:
    student = input("Type student for search:")
    studentFound = searchStudent(
        student1, student2, student3, student4, student)
    if (studentFound):
        print("\nThe student is: \n", studentFound)
    else:
        print("\nThe student not exist")
    shouldAdvanceSemestry = bool(input(
        "Do you want to advance the semestry type the next: \n Yes: 1 \n No: 0 \n:"))
    if(shouldAdvanceSemestry):
        advanceSemestry(student1, student2, student3, student4)

    studentsInRisk = whoAreInRisk(student1, student2, student3, student4)

    print("\n The students in risk with average less than 3.4 are: \n", studentsInRisk)


initialization()
