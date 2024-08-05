from random import randrange as rd
x = int(input("x = "))
while(x < 1 or x > 1000):
    x = int(input("x= "))
y = rd(1,4)
sum = 0
answer = 0
for i in range(x):
    if sum + y <= x:
        y = rd(1,4)
        sum += y
        answer += 1
print(answer)


