def numberOfOcurrencies(number: int) -> dict:
    numberInString = str(number)
    dictionary = {}
    dictionary[0] = numberInString.count('0')
    dictionary[1] = numberInString.count('1')
    dictionary[2] = numberInString.count('2')
    dictionary[3] = numberInString.count('3')
    dictionary[4] = numberInString.count('4')
    dictionary[5] = numberInString.count('5')
    dictionary[6] = numberInString.count('6')
    dictionary[7] = numberInString.count('7')
    dictionary[8] = numberInString.count('8')
    dictionary[9] = numberInString.count('9')

    return dictionary

number = int(input('Type an number of ten ciphers: '))
print(numberOfOcurrencies(number))