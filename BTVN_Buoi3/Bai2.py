k = int(input("k= "))

a = []

for i in range(k):
    a.append(int(input()))

n = int(input("n= "))
m = int(input("m= "))

if n*m>k:
    print("khong the tao ma tran")
else:
    matrix = []
    index = 0
    for i in range(n):
        row =[]
        for j in range(m):
            row.append(a[index])
            index += 1
        matrix.append(row)

    for row in matrix:
        print(row)