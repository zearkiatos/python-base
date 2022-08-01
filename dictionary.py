emptyDictionary = {}

print(type(emptyDictionary))

dictionary = {"Alicia": "321 456 29 73", "Bastian": "30 248 37 00", "Armando": "316 754 89 38"}

print(dictionary)

dictionary["Juan"] = "311 286 25 27"

print(dictionary)

daySchedule = {}

daySchedule[6] = "Start the day"

print(daySchedule)

shoppingCart = {}

shoppingCart["Leche"] = 2000

print(shoppingCart)

shoppingCart["Leche"] = 2500

print(shoppingCart)

print("Leche" in shoppingCart)

print(shoppingCart.get("Huevo", "Huevo not exist"))

print(shoppingCart.get("Leche", "Leche not exist"))

print(len(dictionary))

