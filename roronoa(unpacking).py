def fun():
    a = 10
    b = 20
    c = 30
    return a,b,c

print(fun())

an1, an2, an3=fun()#unpacking
print(an1)
print(an2)
print(an3)

print(*fun())

