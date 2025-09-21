s={1,2,3,4,5,}
for i in s:
    print(i)
   

a={1,2,3,4,5}
a.add(6)
print(a)
a.update([7,8])
print(a)

a.remove(8)#if element present in the set remove ,if element non in set through error
print(a)
a.discard(7)
print(a)
a.discard(9)#if element present in the set remove ,if non in it  not through error
print(a)
a.pop()
print(a)
a.clear()
print(a)