n = int(input("n= "))
a= set()
for i in range(n):
    k = int(input())
    a.add(k)
b = int(input())
answer = set()
total = 0
for i in sorted(a):
    if total +i <= b:
        total += i
        answer.add(i)
print(answer)
