n = int(input("n= "))
k = input().split()
a = []
if len(k) <=n:
    for i in k:
        a.append(i)
b = tuple()
count = 0
for i in a:
    b += (i,)
    if i.isdigit():
        count+=1
print(b)
print(count)