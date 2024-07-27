n = int(input("n= "))

a = 0
b = 1

for i in range(1,n):
    f = a + b
    a = b
    b = f
print(f)

