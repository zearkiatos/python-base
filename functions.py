def quarter(x: float) -> float:
    return x**2


print(quarter(4))


def cube(x: float) -> float:
    return x*x*x


print(cube(2))


def rectArea(height: float, width: float) -> float:
    return height*width


print(rectArea(20, 10))


def rectArea2(height: float, width: float) -> float:
    area = height*width
    return area


print(rectArea2(20, 10))


def readInteger() -> int:
    return int(input())


print(readInteger())


def cube2() -> int:
    x = int(input('Type the value: '))
    return x*x*x


print(cube2())


def lastCipher(number: int) -> int:
    return number % 10

print(lastCipher(10))
