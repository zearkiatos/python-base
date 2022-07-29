from typing_extensions import Never


def evalANumber(number: int) -> int:
    if (number < 0):
        result = -1
    elif (number < 1000):
        result = 0
    elif (number <= 10000):
        result = 1
    else:
        result = 2
    return result


def initializationProgram() -> Never:
    number = int(input('Type a number: '))
    result = evalANumber(number)
    print('The number evaluation is: ', result)


initializationProgram()
