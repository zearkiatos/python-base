num1 = int(input('Type a number: '))
num2 = int(input('Type a second number: '))
num3 = int(input('Type a third number: '))

howMany = 0

if num1 % 2 == 0:
    howMany += 1
if num2 % 2 == 0:
    howMany += 1
if num3 % 2 == 0:
    howMany += 1

print('The three numbers typed there are ', howMany, ' pairs')
