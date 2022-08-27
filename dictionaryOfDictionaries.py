directory = {}

directory["Juan"] = {"cellphone": "300 235 87 45",
                     "mail": "juan@gmail.com", "birthday": "10-04"}

directory["Luis"] = {"cellphone": "311 986 47 00",
                     "mail": "luis@hotmail.com", "birthday": "01-03"}

directory["Ana"] = {"cellphone": "320 700 62 15",
                    "mail": "ana@yahoo.com", "birthday": "15-09"}

directory["Maria"] = {"cellphone": "312 958 88 50",
                      "mail": "maria@tamalo.com", "birthday": "31-10"}

print(directory)


for element in directory:
    print(element, "->", directory[element])
