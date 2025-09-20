''' A tuple is a collection in Python.
Similar to a list, but immutable (cannot be changed after creation)
Ordered, indexed, and allows duplicates.
'''

a=1,89,0,9
print(type(a))
a=(5)
print(type(a))
a=(5,)#comma change the type
print(type(a))


mixed=(1,"hello",3.14,True)
print(mixed)

t=(100,20,30,40)
print(t[0])
print(t[-1])


#sliceing
t=(12,23,454,56,76,87)
print(t[::2])
t=list(t) 
print(t)   
t[0]=1
t[2]=2
t[4]=3
print(list(t))
t=tuple(t)
print(t)