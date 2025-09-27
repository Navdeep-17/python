a= (lambda a,b:a**b)(2,3)
print(a)#here we cannot call function again

func=(lambda a,b:a**b)
c=func(20,2)
print(c)#here we call lambda function
 
l = lambda n: "Even" if n%2==0 else "Odd"
print(l(7))#odd even using lambda

add=lambda x,y:x+y
print(add(10,20))

#string operation

reverse = lambda s: s[::-1]
print(reverse("String"))

reverse = lambda s: s[-1]
print(reverse("String"))


def func (x):
    for i in x:
        if i %2==0:
            print("even")
            
        else:
            print("odd")
func([1,2,3,4])

lst = [10,13,24,15,25,30,66]#filter using function
def fun (x):
    if x % 2 == 0:
        return True# if "if" condition true it store in ans
    else:
        return False
    
ans = list(filter (fun, lst))#list is optional
print(ans)

l=[1,2,3,4,5]#filter using lambdafunction
n=list(filter(lambda x :x%2==0,l ))
print(n)
