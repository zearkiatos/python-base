def isDivisible(n: int, d: int) -> int:
    result = 0
    if (2*d == 0 or d == 0):
        result = 0
    elif (n % (2*d) == 0):
        result = 2
    elif (n % d == 0):
        result = 1
    else:
        result = 0
    return result

print(isDivisible(1000000,1000000))

