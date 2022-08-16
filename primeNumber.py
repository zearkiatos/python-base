def is_prime_number(number: int) -> bool:
    isPrime = True

    for i in range(2, number):
        if (number % i == 0):
            isPrime = False
            break
    return isPrime


print(is_prime_number(41))
