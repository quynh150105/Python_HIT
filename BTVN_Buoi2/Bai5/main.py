n = int(input("n= "))

for i in range(1, n+1):
    tong = 0
    m = i
    temp = i
    while(temp>0):
        a = temp%10
        tong += pow(a,3)
        temp = temp//10
    if(tong == m):
        print(m," la so armstrong bac 3 ")
        


