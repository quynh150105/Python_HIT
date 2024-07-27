n = int(input("n= "))
m = int(input("m= "))
sum1 = 0
sum2 = 0
for i in range(1,n):
    if n%i==0:
        sum1 += i
for i in range(1,m):
    if m%i==0:
        sum2 += i

if n == sum2 and m == sum1:
    print("Amicable")

