n = int(input("n= "))

for j in range(1, n+1):
    tong = 0

    i = 1

    while(i<j):
        if(j%i==0):
            tong += i
        i +=1

    if(tong == j):
        print(j, " la so hoan hao")
    