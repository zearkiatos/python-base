def characters_ocurrencies(string: str, character: str) -> int:
    ocurrencies = 0
    i = 0
    while(i < len(string)):
        if(string[i] == character):
            ocurrencies += 1
        i += 1
    return ocurrencies


print(characters_ocurrencies('Dinosaurs', 's'))

print(characters_ocurrencies('The White House', 'a'))

print(characters_ocurrencies('The White House', 'W'))

print(characters_ocurrencies('The White House', 'h'))

print(characters_ocurrencies('The White House', 'H'))
