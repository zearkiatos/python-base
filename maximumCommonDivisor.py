def maximum_common_divisor(n1: int, n2: int) -> int:
    n = min(n1, n2)
    found = False
    while (not found):
        if(n1 % n == 0 or n2 % n == 0):
            found = True
        else:
            n = n - 1
    return n


print(maximum_common_divisor(20, 10))
