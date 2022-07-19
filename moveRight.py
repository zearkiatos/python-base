x1 = int(input('Type x1 value: '))
x2 = int(input('Type x2 value: '))
x3 = int(input('Type x3 value: '))

temp = x1
x1 = x3
x3 = x2
x2 = temp
print("X1: "+str(x1))
print("X2: "+str(x2))
print("X3: "+str(x3))
