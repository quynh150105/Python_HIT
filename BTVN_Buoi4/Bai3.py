n,m = map(int,input().split())

arr = list(map(int,input().split()))

A = set(map(int,input().split()))

B = set(map(int,input().split()))

answer = 0

for i in arr:
    if i in A:
        answer +=1
    elif i in B:
        answer -=1
    else:
        answer += 0
print(answer)
