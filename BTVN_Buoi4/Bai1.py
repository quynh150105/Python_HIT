str = '0123456789'
tup = tuple(str)
print(f"tuple ban dau la: {tup}")
answer = ()
for i in tup:
    a = int(i)
    answer += (a,)
print(f"new tuple: {answer}")
sum = 0
for i in answer:
    sum += i
print(f"tbc la: {sum/len(answer)}")
