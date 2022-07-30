
def clasifiedGift(id: int) -> str:
    calification = ''
    if (id < 100):
        return 'The gift id must be a number between 100 and 999'
    if(isPalindrome(id) and not isPar(id)):
        calification = 'girl'
    elif (isPalindrome(id) and isPar(id)):
        calification = 'boy'
    elif (isPar(id) and not isPalindrome(id)):
        calification = 'man'
    elif (not isPar(id) and not isPalindrome(id)):
        calification = 'woman'
    return calification


def isPar(id: int) -> bool:
    return id % 2 == 0


def isPalindrome(id: int) -> bool:
    stringId = str(id)
    invertId = stringId[::-1]
    return invertId == stringId


print(clasifiedGift(300))

