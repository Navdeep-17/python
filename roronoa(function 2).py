#lambda function is a small anonymous funtion,it take any number of argument ,but can only have one function


x= lambda a: a+5
print(x(6))

x= lambda a , b : a+b
print(x(1,9))

def myfunc (n):
    return lambda a:a*n
mymultipy= myfunc(10)
print(mymultipy(10))
