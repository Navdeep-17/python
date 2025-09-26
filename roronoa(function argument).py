def power(a,b,c):#positional argument
   d=c+a**b
   print(d)
power (2,5,7)#here value posision change,result also change


def power(a,b,c=0):#default argument
   print(a,b,c)
power (2,5,7)#here 7 c is update


def power(a,b,c):#key argument
   print(a,b,c)
power (a=3,b=3,c=3)


def pizza_toppings (*toppings):#variable length argument
     print(toppings)
pizza_toppings ("cheese","onion","olives")


def student_data(**data):#variable key length argument
    print(data)
student_data(name ="jagan", age=21)