def createStudent(name: str, code: str, genre: str, career: str, average: float, ssc: float) -> dict:
    student = {
        "name": name,
        "code": code,
        "genre": genre,
        "career": career,
        "average": average,
        "ssc": ssc
    }
    return student


student1 = createStudent("Juan Pérez", "201824736",
                         "male", "Biology", 3.78, 0.7)
student2 = createStudent("Ana Gavalda", "201724736",
                         "female", "Polic Scientics", 4.25, 3.5)
student3 = createStudent("Bastien Bosa", "201815217",
                         "male", "Economic", 3.21, 2.3)
student4 = createStudent("Catalina Gómez", "201715400",
                         "female", "Art", 3.8, 4)


def searchStudent(student1: dict, student2: dict, student3: dict, student4: dict, search: str) -> dict:
    studentFound = None
    if(student1["name"] == search):
        studentFound = student1
    if(student2["name"] == search):
        studentFound = student2
    if(student3["name"] == search):
        studentFound = student3
    if(student4["name"] == search):
        studentFound = student4
    return studentFound


def initialization() -> None:
    student = input("Type student for search:")
    studentFound = searchStudent(
        student1, student2, student3, student4, student)
    if (studentFound):
        print("\nThe student is: \n", studentFound)
    else:
        print("\nThe student not exist")
initialization()
