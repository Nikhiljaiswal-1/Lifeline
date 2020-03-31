n=int(input())
temp=n
t=0
d=0
while n!=0:
    d=n%10
    t=t+d**3
    n=n//10
print(t)    
if t==temp:
     print("armstrong")
else:
    print("notarmstrong")
    
    
    
