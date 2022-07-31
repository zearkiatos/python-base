def moreA(string1: str, string2: str, string3: str, string4: str) -> str:
    moreA = string1
    if (string2.upper().count('A') > moreA.upper().count('A')):
        moreA = string2
    if (string3.upper().count('A') > moreA.upper().count('A')):
        moreA = string3
    if (string4.upper().count('A') > moreA.upper().count('A')):
        moreA = string4
    return moreA

print(moreA('Acampar','fresa','carro','manzana'))