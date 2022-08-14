def factorial(n: int) -> int:
    count = 0
    factorialResult = 1
    if (n == 0):
        factorialResult = 1
    else:
        while(n > count):
            factorialResult *= (count+1)
            count += 1

    return factorialResult


def user_interface_factorial() -> None:
    number = int(input("Type a number: "))
    factorialResult = factorial(number)
    print("The factorial is for {0} is {1}".format(number, factorialResult))

user_interface_factorial()
