n = int(input("n= "))

sum = 0

for i in range(1,2*n + 2):
    if(i %2 != 0):
        sum += i
    else:
        sum -= i
print("tong la: ", sum)