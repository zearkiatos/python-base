def menor_position_list(numbers: list) -> int:
    less = numbers[0]
    position = 0
    for number in numbers:
        if (number < less):
            less = number
            position = numbers.index(number)
    return position


numbers = [4, -1, -4, 5, 1, 6, 10, 17, 31, -14, -61]
print(menor_position_list(numbers))
