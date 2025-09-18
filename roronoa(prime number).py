n= int(input(""))
if( n <=1):
    print("not prime number")
elif(n==2 or n==3 or n==5 or n==7 ):
    print("prime number")
elif(n%2==0 or n%3==0 or n%5==0 or n%7==0 ):
    print("not prime number")
else:
    print("prime number")
    
# anouther way
n=int(input())
count = 0

for i in range (1,n+1):
    if n%i==0:
        count+=1
if count==2: