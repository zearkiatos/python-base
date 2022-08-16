def character_ocurrencies(strings: str, character: str) -> int:
    ocurrencies = 0
    for item in strings:
        if(item == character):
            ocurrencies += 1
    return ocurrencies


print(character_ocurrencies('Dinosaurs', 's'))

print(character_ocurrencies('The White House', 'a'))

print(character_ocurrencies('The White House', 'W'))

print(character_ocurrencies('The White House', 'h'))

print(character_ocurrencies('The White House', 'H'))