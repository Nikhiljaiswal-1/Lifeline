n=int(input("enter a no:"))
temp=n
rev=0
while n!=0:
    d=n%10
    rev=rev*10+d
    n=n//10
   
if rev==temp:
    print( temp," is palindrome")
else:
    print( temp," is Not palindrome")
    
