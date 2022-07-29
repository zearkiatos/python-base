import math
from tkinter import Y
x = int(input('Type a  number: '))

if x % 2 == 0:
    print(x, ' is pair')
    print('Do you know that to number 2 is the unique pair prime number?')
else:
    print(x, ' is unpair')
    print('Do you know that mutiply two unpair numbers always return a umpair result?')

x = int(input('Type a number: '))

if x < 0:
    print('The negative number', x, ' is not valid here.')
    y = x
    x = 42
    print('Decided use the number 42 instead ', Y)

print('The quarter of ', x, ' is', math.sqrt(x))
