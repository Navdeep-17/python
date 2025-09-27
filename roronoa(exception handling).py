print("secure connrction has been enabled")
try:
    p=int(input("enter the principal amount"))
    r=20
    t=int(input("enter the time"))
except:
    print("please enter the data in numbers")
else:
    si=(p*r*t)/100
    print(si)
print("secure connection has been terminated")