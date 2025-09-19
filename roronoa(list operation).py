n=[1,2,3,4,5]
print(n)
print(n[0])
print(n[-1])
print(n[2:4])
print(n + [6,7])
del n


a=[1,2,1,4,1,3,1]
for i in a:
    if i==1:
        a.remove(i)
print(a)
del (a[::2])
print(a)

st1 =[10,20,30,40,50,60,70,80]
st2=st1[:]#here a address of list change
print(st2)
print(id(st1))
print(id(st2))
