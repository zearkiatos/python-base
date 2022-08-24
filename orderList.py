def main_program() -> None:
    key_word_to_close = 'terminar'
    word = ''
    option = ''
    word_list = []
    while key_word_to_close != option:
        word = input('\nPlease type a new word ')
        add_word(word_list, word)
        word_list = custom_sort(word_list)

        print('\nThe list has this values \n', word_list)
        option = input(
            '\n Do you want to continue? (Type "terminar" if you do not want to continue)')


def add_word(word_list: list, new_word: list) -> None:
    word_list.append(new_word)


def custom_sort(word_list: list) -> list:
    sentinel = ''
    for i in range(0, len(word_list)):
        for j in range(i+1, len(word_list)):
            if(word_list[i].upper() > word_list[j].upper()):
                sentinel = word_list[i]
                word_list[i] = word_list[j]
                word_list[j] = sentinel

    return word_list


def sort(word_list: list) -> list:
    word_list.sort()


main_program()
