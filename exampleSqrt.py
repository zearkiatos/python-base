from math import sqrt
possitiveNumber = False
while (not possitiveNumber):
    x = float(input("Type a possitive number: "))
    possitiveNumber = x >= 0
    if (possitiveNumber):
        print("\nThe sqrt of {0} is {1}".format(x, sqrt(x)))
    else:
        print("\nYou must type a possitive number")