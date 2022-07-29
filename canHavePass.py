def canHavePassV1(age: int) -> bool:
    if not (age >= 16):
        return False
    else:
        return True


def canHavePassV2(age: int) -> bool:
    if(age < 16):
        return False
    else:
        return True


def canHavePassV3(age: int) -> bool:
    can = True
    if (age < 16):
        can = False
    return can


def canHavePassV4(age: int) -> bool:
    can = False
    if (age >= 16):
        can = True
    return can


def canHavePassV5(age: int) -> bool:
    return age >= 16


print(canHavePassV1(20))
print(canHavePassV2(20))
print(canHavePassV3(20))
print(canHavePassV4(20))
print(canHavePassV5(20))