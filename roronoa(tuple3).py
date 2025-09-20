#packing
p=1,2,3,4
print(p)
a,a1,a2,a3 = p
print( a,a1,a2,a3)

#nested tuple
l=(1,(1,2),(1,2,3))
print(l)
print(l[1])

#acess list inside tuple
a=("alice",25,["py","java"])
print(a)
a[2].append("c++")
print(a)
