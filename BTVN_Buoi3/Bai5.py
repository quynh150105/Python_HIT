n = int(input("n= "))

while(n<1 or n>100):
    n = int(input("n= "))

number = input()

lst = number.split()

lst1 = []

if len(lst) == n:
    lst1 = [int(x) for x in lst]

count = 0

answer = []

for i in lst1:
    if i%10==1 or i%10==3 or i%10==5 or i%10==7 or i%10==9:
        count +=1
        answer.append(i)

print(count)
for i in answer:
    print(i, end = " ")