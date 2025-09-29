print("Execution start")
lst = [10,20,30,0,50,60]
d={1:"c",2:"c++",3:"python", 4:"java"}
try:
    n= int(input("enter a key:"))
    print(d[n])
    num = int(input("enter numerator:"))
    print(lst[num])
    den= int(input("enter denominator:"))
    print(lst[den])
    ans = lst[num] / lst [den]
    print(ans)
except KeyError:
    print("enter a valid key")
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
print("Execution stop")