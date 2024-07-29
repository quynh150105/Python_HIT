k = int(input("k= "))
a = []
for i in range(k):
    a.append(int(input()))
n = int(input("n= "))
m = int(input("m= "))
if(n*m>k):
    print("No")
else:
    answer = []
    index = 0
    for i in range(n):
        row = []
        for i in range(m):
            row.append(a[index])
            index += 1
        answer.append(row)

    for i in answer:
        print(i)
    










