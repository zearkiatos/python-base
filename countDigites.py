def count_digits(number: int) -> int:
    count = 0
    finish = False
    while(not finish):
        if(number == 0):
            finish = True
        else:
            count += 1
            number //= 10
    return count


def user_interface_count_digits() -> None:
    number = int(input("Type a number: "))
    digits = count_digits(number)
    print("\nThe number of digits is {}".format(digits))


user_interface_count_digits()
