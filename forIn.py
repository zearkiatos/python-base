strings = "One hundred years alone"

for character in strings:
    print(character)


def sumatory() -> int:
    result = 0
    for i in range(1, 1001):
        result += i
    return result


print(sumatory())
