PI = 3.14159


def fahrenheitToCentigrade(degrees: float) -> float:
    return round((degrees-32)*(5/9), 2)


print(fahrenheitToCentigrade(55.4))


def centigradeToFahrenheit(degrees: float) -> float:
    return round((degrees*9/5+32), 2)


print(centigradeToFahrenheit(13))


def radianToGrade(radianes: float) -> int:
    return round((radianes*360)/(2*PI))


print(radianToGrade(6.2832))


def gradeToRadian(grade: int) -> float:
    return round((grade*2*PI)/360, 4)


print(gradeToRadian(360))

def invertNumber(number:int) -> int:
    numberConverted = str(number)
    numberInverted = numberConverted[::-1]
    return int(numberInverted)

def invertNumber2(number:int)->int:
    units = number%10
    number//=10
    decens = number%10
    number//=10
    cents= number%10
    number//=10
    mills= number%10
    numberInverted = (units*1000)+(decens*100)+(cents*10)+mills
    return numberInverted

print(invertNumber(3719))

print(invertNumber2(3719))
