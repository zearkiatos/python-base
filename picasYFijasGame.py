def secretNumber(number: int, tryNumber: int) -> dict:
    dictionary = {}
    dictionary['PICAS'] = getPica(number, tryNumber)
    dictionary['FIJAS'] = getFija(number, tryNumber)
    return dictionary


def getPica(number: int, tryNumber: int) -> int:
    numberStr = str(number)
    tryNumberStr = str(tryNumber)
    pica = 0
    if (numberStr[1:].find(tryNumberStr[0]) != -1):
        pica += 1
    if (numberStr[2:].find(tryNumberStr[1]) != -1 or numberStr[0] == tryNumberStr[1]):
        pica += 1
    if (numberStr[0:2].find(tryNumberStr[2]) != -1 or numberStr[3] == tryNumberStr[2]):
        pica += 1
    if (numberStr[0:3].find(tryNumberStr[3]) != -1):
        pica += 1
    return pica


def getFija(number: int, tryNumber: int) -> int:
    numberStr = str(number)
    tryNumberStr = str(tryNumber)
    fija = 0
    if (numberStr[0] == tryNumberStr[0]):
        fija += 1
    if (numberStr[1] == tryNumberStr[1]):
        fija += 1
    if (numberStr[2] == tryNumberStr[2]):
        fija += 1
    if (numberStr[3] == tryNumberStr[3]):
        fija += 1
    return fija


def initialization() -> None:
    print("***** Pica y Fijas *****\n")
    print("Player 1 Turn:\n")
    number = int(input("Type the secret number: "))
    print("\nPlayer 2 Turn:\n")
    tryNumber = int(input("Type the number that you try to guess: "))
    dictionary = secretNumber(number, tryNumber)
    print(dictionary)


initialization()
