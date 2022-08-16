def is_palindrome(phrase: str) -> bool:
    phrasePrepared = phrase.lower().replace(' ', '')
    return phrasePrepared[:] == phrasePrepared[::-1]


print(is_palindrome('Isaac no ronca asi'))

print(is_palindrome('Sometamos o matemos'))

print(is_palindrome('Hello World!'))
