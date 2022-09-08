import math
tuple = (4, 7, 2, 4, 7, 9, 2, 9)
print(tuple)

print(type(tuple))

coordenades = (3, 6, 3)

print(coordenades)

print(type(coordenades))

coordenades = 3, 6, 3
print(type(coordenades))

x = 2

y = 3

width = 7
height = 4

rectangle = ((x, y), (width, height), "red")

print(rectangle)

empty_tuple = ()

type(empty_tuple)

print(len(empty_tuple))

unit_tuple = (5,)

type(unit_tuple)

x = (5)

print(type(x))

print(coordenades[1])

print(rectangle[0:2])

print(rectangle[-1])

print(len(rectangle))

corner, dimention, color = rectangle

print(corner)


def calculation_area_and_perimeter(rectangle: tuple) -> tuple:
    dimension = rectangle[1]
    width, height = dimension

    area = width*height

    perimeter = (width + height)*2

    return (area, perimeter)


area, perimeter = calculation_area_and_perimeter(rectangle)


print(area)

print(perimeter)


def calculation_distance(point_1: tuple, point_2: tuple) -> float:
    delta_x = abs(point_1[0] - point_2[0])
    delta_y = abs(point_1[1] - point_2[1])

    distance = math.sqrt(delta_x**2 + delta_y**2)

    return distance

p1 = (1,2)

p2 =  (4,6)

print(calculation_distance(p1, p2))
