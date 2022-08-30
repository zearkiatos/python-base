M = [[1, 2, 3], [2, 12, 6], [1, 0, -3], [0, -1, 0]]

print(M)

print(M[0][0])

print(M[0][1])

print(M[0][2])

print(M[1][0])

print(M[1][1])

print("", M[0], "\n", M[1])

a = [0]*6

print(a)

M = [a]*3

print(M)

print("", M[0], "\n", M[2])

M = []

for i in range(0, 3):
    a = [0]*6
    M.append(a)
print(M)

m = int(input("\nType the number of files: "))
n = int(input("\nType the number of columns: "))

M = []

for i in range(0, m):
    M.append([0]*n)

for i in range(0, m):
    for j in range(0, n):
        M[i][j] = float(
            input("\nType the content of for path ["+str(i)+"]["+str(j)+"]: "))

print("\nThe complete matriz is: ")

for i in range(0, m):
    print(M[i])

a = [[1, 0], [0, 1], [0, 0]]

print(len(a))

print(len(a[0]))
