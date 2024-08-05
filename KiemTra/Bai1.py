a = (1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,4,4,4,4,4)
answer = ''
for i in a:
    k = i
    if(a.count(i) % 5 == 0 and a.count(i) % 10 != 0):
         print(k)
   


