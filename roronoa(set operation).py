#set operation
a={9,8,7,6,5}
b={6,5,4,3}
print(a|b)
print(a & b)
print(b-a)
print(a^b)

print("\n")
  
  
#set method
s = {1,2,3,4}
print(len(s))
print(max(s))
print(min(s))
print(sum(s))

print("\n")

c={1,2,3,4,5}
d={1,2}
print(c.issubset(d))#check cin d or not
print(d.issubset(c))
print(c.issuperset(d))#check cin d or not
print(d.issuperset(c))
print(d.isdisjoint(c))#print true if both set has diffrent element ,if one element are same in both set return false

print("\n")


s=frozenset([1,2,3])
print(s)
'''s.add(100)
print(s)# it not allow to add,if these throw error
'''