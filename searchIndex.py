def search_index(output: list, element_searched: int) -> int:
    index = -1
    for number in output:
        if (number == element_searched):
            index = output.index(element_searched)
            break

    return index


element_list = [2, 1, 2, 20, 1]


print(search_index(element_list, 50))
