A = {2023600638,2023600634,2023600321,2022600789}
B = {2023600123,2023600638,2020600123,2023600789}
print(f"A= {A}")
print(f"B= {B}")
if A&B:
    print(f"cac sv dk tai 2 ban la: {A&B}")
else:
    print("khong co sv nao dk tai 2 ban")
print(f"Danh sach tong hop cac sv dk tai 2 ban la: {A|B}")
print(f"cac sv dk tai ban 1 ma ko dk tai ban 2 la: {A-B}")


