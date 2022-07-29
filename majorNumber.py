def major(num1: int, num2: int, num3: int, num4: int) -> int:
    temp = num1
    if num2 >= temp:
        temp = num2
    if num3 >= temp:
        temp = num3
    if num4 >= temp:
        temp = num4
    return temp


def majorv1(a: int, b: int, c: int, d: int) -> int:
    if (a >= b) and (a >= c) and (a >= d):
        return a
    elif (b >= a) and (b >= c) and (b >= d):
        return b
    elif (c >= a) and (c >= b) and (c >= d):
        return c
    else:
        return d


def majorv2(a: int, b: int, c: int, d: int) -> int:
    if (a >= b) and (a >= c) and (a >= d):
        respuesta = a
    elif (b >= a) and (b >= c) and (b >= d):
        respuesta = b
    elif (c >= a) and (c >= b) and (c >= d):
        respuesta = c
    else:
        respuesta = d
    return respuesta


print(major(8, 12, 32, 5))

print(majorv1(8, 12, 32, 5))

print(majorv2(8, 12, 32, 5))
