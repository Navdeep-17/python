# function is block of code which only run when it is called

def myfunction(fname):
    print(fname+" targaryen")
myfunction("aegon")
myfunction("daenerys")


def myfunc(fname,lname):
    print(fname +""+ lname)
myfunc("aegon","targaryen")
myfunc("daenerys","targaryen")


def my_function(*kids):
    print("youngest kid is:"+kids[2])#[2] index number
    print(kids)
my_function("aegon","daenerys","jonsnow")

def my_function(**kids):
    print("youngest kid is:"+kids["lname"])
my_function(fname="jennifer",lname="lawrence")


def family(child3,child2,child1):
    print("youngest kid is:"+  child3)
family("emma","boa","robin")

def ctry(country="norway"):
    print("i am from "+ country)
ctry("fin land")
ctry()
ctry("india")

def eat(food):
    for x in food:
        print(x)
fruit=["apple","banana","cherry"]
eat(fruit)

def myfunc(x):
    return x*5
print(myfunc(5))
print(myfunc(6))
