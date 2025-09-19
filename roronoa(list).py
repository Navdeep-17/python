a=[1,2,3,4,5]
b=[7,8]
print(a)
a.append(6)
print("Append function:",a)
a.insert(2,2.5)
print("Insert function:",a)
a.extend(b)
print("Extend 1 function:",a)
a.extend([9,10])
print("Extend 2 function:",a)
a.pop(10)
print("pop function",a)
a[9]=8.5
print("modify 1 function",a)
a[1:9]=[23,34,45,56]
print("modify 2 function",a)
a[::2]=[1,2,3]
print("modify 3 function",a)
a.remove(1)
print("remove",a)


