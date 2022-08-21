my_list = []

my_list.append(5)

my_list.append(27)

my_list.append(3)

my_list.append(12)

print(my_list)

print(my_list.count(12))

my_list.extend([5, 9, 5, 11])

print(my_list)

print(my_list.index(9))

my_list.reverse()

print(my_list)

my_list.sort()

print(my_list)

print(my_list.remove(5))

print(my_list)

my_list_copied = my_list.copy()

print(my_list_copied)

deleted = my_list.pop(5)
print(deleted)

my_list.clear()

print(my_list)
