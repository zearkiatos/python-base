NOT_ALLOW_CHARACTERS = [' ', '.', ',']


def commonestLetter(string: str) -> str:
    list_string = list(string.upper())
    gratest_letter_appear = ''
    gratest_quantity_letter_appear = 0
    letter_and_quantity = {}

    for letter in list_string:
        if (not letter in NOT_ALLOW_CHARACTERS):
            if (not letter in list(letter_and_quantity)):
                letter_and_quantity[letter] = 0
            letter_and_quantity[letter] += 1

    for letter in list(letter_and_quantity):
        if (letter_and_quantity[letter] > gratest_quantity_letter_appear  or (gratest_quantity_letter_appear == letter_and_quantity[letter] and letter > gratest_letter_appear)):
            gratest_letter_appear = letter
            gratest_quantity_letter_appear = letter_and_quantity[letter]

    return gratest_letter_appear


print(commonestLetter('Hello World!'))
