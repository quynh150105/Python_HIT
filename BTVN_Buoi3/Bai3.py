s1 = input("s1= ")
s2 = input("s2= ")

print(f"s1 sau khi dao nguoc la: {s1[::-1]}")

a = int(input("a= "))
b = int(input("b= "))
while a<1 or a >=b or b > len(s2):
    a = int(input("a= "))
    b = int(input("b= "))

print(f"s2 sau khi dao la: {s2[b:a-1:-1]}")

s3 = ""
for i in range(len(s1)):
    if i %2 !=0:
        s3+=s1[i]
print(f"s3 la: {s3}")

s4 = ""
if  len(s1) >len(s2):
    n = len(s2)
    temp = s1[n:len(s1)+1]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if i==j:
                s4 += s1[i] + s2[j]
    print(f"s4 la: {s4 + temp}")
elif len(s1) <len(s2):
    n = len(s1)
    temp = s2[n:len(s2)+1]
    for i in range(len(s2)):
        for j in range(len(s1)):
            if i==j:
                s4 += s2[i] + s1[j]
    print(f"s4 la: {s4 + temp}")

temp1 = s1
temp2 = s2
s1 = s1.replace(s1[0], temp2[0])
s2 = s2.replace(s2[0], temp1[0])
print(f"s1 sau khi doi la: {s1}")
print(f"s2 sau khi doi la: {s2}")
