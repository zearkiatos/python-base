a = [1, 2, 3]

b = [1, 2, 3]

c = a

print(a)

print(b)

print(c)

print(a == b)

print(a == c)

print(b == c)

print(a is b)

print(a is c)

c[0] = 4

print(c)

print(a)

print(b)

def duplicate(listVariables: list)->None:
    for i in range(0, len(listVariables)):
        listVariables[i] = listVariables[i]*2

numbers = [1,2,3,4,5]

print(numbers)

duplicate(numbers)

print(numbers)

a = [1,2,3]

b = a[:]

print(a)

print(b)

print(a == b)

print(a is b)