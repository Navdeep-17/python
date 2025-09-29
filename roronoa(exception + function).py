def fun2():
    print("fun2 execution start")
    try:
        num =int(input())
        den =int(input())
        ans=num / den
        print(ans)
        print("fun2 execution stop")
    except Exception as e:
        print(e)
def fun1():
    print("fun1 execution start")
    fun2()
    print("fun1 execution stop")
def main():
    print("main execution start")
    fun1()
    print("main execution stop")
main()