def function_a() -> None:
    print('You have choosed the a menu')


def function_b() -> None:
    print('You have choosed the b menu')


def function_c() -> None:
    print('You have choosed the c menu')


def function_d() -> None:
    print('You have choosed the d menu')


print('Main menu')
print('Option a')
print('Option b')
print('Option c')
print('Option d')

x = input('Select your option: ')

if x == 'a':
    function_a()
elif x == 'b':
    function_b()
elif x == 'c':
    function_c()
elif x == 'd':
    function_d()
else:
    print('Invalied choose')
