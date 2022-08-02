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

print("The students are: \n", "Student 1: \n", student1,
      "\n Student 2:\n", student2,
      "\n Student 3:\n", student3,
      "\n Student 4:\n", student4)


def majorAverage(student1: dict, student2: dict, student3: dict, student4: dict) -> dict:
    studentWithMajorAverage = student1
    if (student2["average"] >= studentWithMajorAverage["average"]):
        studentWithMajorAverage = student2
    if (student3["average"] >= studentWithMajorAverage["average"]):
        studentWithMajorAverage = student3
    if (student4["average"] >= studentWithMajorAverage["average"]):
        studentWithMajorAverage = student4
    return studentWithMajorAverage


result = majorAverage(student1, student2, student3, student4)
print("\n", result)


def countWomen(student1: dict, student2: dict, student3: dict, student4: dict) -> int:
    womenCounter = 0
    if (student1["genre"] == "female"):
        womenCounter += 1
    if (student2["genre"] == "female"):
        womenCounter += 1
    if (student3["genre"] == "female"):
        womenCounter += 1
    if (student4["genre"] == "female"):
        womenCounter += 1
    return womenCounter


def thereAreSmartWomen(student1: dict, student2: dict, student3: dict, student4: dict) -> int:
    return (student1["average"] and student1["genre"] == "female") > 4 or (student2["average"] > 4 and student2["genre"] == "female") or (student3["average"] > 4 and student3["genre"] == "female") or (student4["average"] > 4 and student4["genre"] == "female")


print("\n", countWomen(student1, student2, student3, student4))

print("\n", thereAreSmartWomen(student1, student2, student3, student4))
