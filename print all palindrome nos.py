
flag=0
for i in range(101,200):
    rev=0
    temp=i
    while i!=0:
        d=i%10
        rev=rev*10+d
        i=i//10
    if temp==rev:
       print(temp)
    

