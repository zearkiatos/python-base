def partial_running_with_sentinel(numbers: list, search: int) -> int:
    i = 0
    position = -1
    already_found = False
    while i < len(numbers) and not already_found:
        if (numbers[i] == search):
            already_found = True
            position = i
        i += 1
    return position


list_numbers = [20, 90, 8, 10, 2, 1, 1, 2]

print(partial_running_with_sentinel(list_numbers, 2))


def partial_running_without_sentinel(numbers: list, search: int) -> int:
    i = 0
    position = -1
    while i < len(numbers) and numbers[i] != search:
        i += 1
        if (i == len(numbers)):
            position = -1
        else:
            position = i
    return position


print(partial_running_without_sentinel(list_numbers, 2))
