def main_program() -> None:
    key_word_to_close = 'terminar'
    word = ''
    option = ''
    word_list = []
    while key_word_to_close != option:
        word = input('\nPlease type a new word ')
        add_word(word_list, word)
        sort(word_list)

        print('\nThe list has this values \n', word_list)
        option = input(
            '\n Do you want to continue? (Type "terminar" if you do not want to continue)')


def add_word(word_list: list, new_word: list) -> None:
    word_list.append(new_word)


def sort(word_list: list) -> list:
    word_list.sort()


main_program()
