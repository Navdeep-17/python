def func(x):
    a=sum(x)
    print(a)
func([1,2,3,4,5])
    

from functools import reduce

lst = [1,2,3,4,5]

def fun (x,y): #sum using reduce function
    return x+y

ans =reduce(fun, lst)
print(ans)

from functools import reduce
lst = [1,2,3,4,5]
ans=reduce(lambda x,y : x+y, lst)#sum using reduce function+lambda function
print(ans)


