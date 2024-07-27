n = int(input("n= "))

sum = 0

while(n>0):
    a = n%10
    sum+= a
    n = n//10

print("tong la: ", sum)