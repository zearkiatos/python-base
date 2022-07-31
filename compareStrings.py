def compareStrings(word1: str, word2: str) -> None:
    if(word1 == word2):
        print("The words are equals")
    elif (word1 < word2):
        print("The word", word1, " is less than the word ", word2)
    else:
        print("The word ", word1, " is grant to the word ", word2)


compareStrings("alma", "blanca")

print("n" in "apple")

a = "string"

print(a.lower())

print(a.upper())

print(a.title())

print(a.swapcase())

a = "Pedro"

b = "A little example"

print(b.replace('little', 'big'))

print(a.find('Pe'))

print(b.count('t'))

print(help('str'))
n1 = 4
n2 = 5
s3 = "2**10 = {0} y {1}*{2} = {3:.3f}".format(2**10, n1, n2, n1*n2)
print(s3)

print(a.find("dro"))
