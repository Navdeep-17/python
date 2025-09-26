def mul ():#without parameter and without retun type
    a=10
    b=2
    c=a*b
    print(c)
mul()

def add(x,y):#with parameter and without return type
    c=x+y
    print(c)
add(10,2)

def sub():#without parameter and with return type
    a=10
    b=20
    c=a-b
    return c
d=sub()#here store the return value
print(d)

def div(x,y):#with parameter
    c=x/y
    return c
d=div(100,10)
print(d)