def order_string(string: str) -> str:
    stringFormated = string.lower().replace(' ', '')
    stringArray = list(stringFormated)
    stringResult = ''
    for i in range(0, len(stringFormated)):
        for j in range(i+1, len(stringFormated)):
            if (stringArray[i] > stringArray[j]):
                temp = stringArray[j]
                stringArray[j] = stringArray[i]
                stringArray[i] = temp

    for character in stringArray:
        stringResult +=character
    return stringResult.lower()


print(order_string("bca"))