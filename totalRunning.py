def sum_total_running_with_while(numbers: list) -> int:
    i = 0
    total = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total


numbers_list = [10, 20, 19, 1, -2]

print(sum_total_running_with_while(numbers_list))


def sum_total_running_with_for_in_range(numbers: list) -> int:
    total = 0
    for i in range(0, len(numbers)):
        total += numbers[i]
    return total


print(sum_total_running_with_for_in_range(numbers_list))


def sum_total_running_with_for_in(numbers: list) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


print(sum_total_running_with_for_in(numbers_list))
