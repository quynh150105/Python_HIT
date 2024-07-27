s = input("nhap ho va ten: ")

s1 = s.strip()

s2 = s1.lower()

s3 = s2.title()

s4 = s3.split()

for i in s4:
    print(i, end = " ")
