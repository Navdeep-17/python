def add(x,y):
    z=x+y
    print(z)
def sub(x,y):
    z=x-y
    print(Z)
def mul(x,y):
    z=x*y
    print(Z)
def div(x,y):
    z=x/y
    print(Z)
def floor(x,y):
    z=x//y
    print(Z)
def exp(x,y):
    z=x**y
    print(Z)
    
print("Calculator")
print("Select operation:")
print("option:add=1,sub=2,mul=3,div=4,floor=5,exp=6")
oper=int(input("enter operation :"))
x=int(input("Enter x value :"))
y=int(input("Enter y value :"))

if oper==1:
       add(x,y)
elif oper==2:
       sub(x,y)
elif oper==3:
       mul(x,y)
elif oper==4:
       div(x,y)
elif oper==5:
       floor(x,y)
elif oper==6:
        exp(x,y)
else:
        print("invalid input")
    