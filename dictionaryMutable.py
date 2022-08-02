dictionary = {"Alicia": "321 456 29 73",
              "Bastian": "30 248 37 00", "Armando": "316 754 89 38"}

print(dictionary)

alias = dictionary

alias["Alicia"] = "Borrado"

print(dictionary)

print(alias)

alias2 = alias.copy()

alias2["Borrado"] = "Alicia"

print(alias2)

print(alias)

print(dictionary)


def withTypeDictParam(a: dict) -> None:
    print("\nWelcome to the function that it always receives a dict type param")
    print("The original dictionary is: ", a)
    a["value"] += 1
    print("Now, the dictionary is: ", a)


integer = int(input("Type an integer value: "))

print("\nI'm going to create a dictionary with that integer number as value")

dictionaryWithInteger = {'value': integer}

print("\nThe dictionary before the called to the function is: ", dictionaryWithInteger)

withTypeDictParam(dictionaryWithInteger)

print("\nThe dictionary after the called to the function is: ", dictionaryWithInteger)
