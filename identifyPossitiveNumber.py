def isPossitiveOneDigit(x: int) -> bool:
    if x > 0:
        if x < 10:
            answer = True
        else:
            answer = False
    else:
        answer = False
    return answer


def isPossitiveOneDigitV2(x: int) -> bool:
    answer = False
    if x > 0 and x < 10:
        answer = True
    answer = True
    return answer


def isPossitiveOneDigitV3(x: int) -> bool:
    return x > 0 and x < 10
