def count_characters_repeated(string: str) -> int:
    count = 0
    countOcurrencies = {}
    for character in string:
        countOcurrencies[character] = 0
    for character in string:
        countOcurrencies[character] += 1
    for character in string:
        if (countOcurrencies[character] > 1):
            count += 1

    print(countOcurrencies)
    return count


print(count_characters_repeated('aloha'))
