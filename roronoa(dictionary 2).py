mycar ={"brand":'ford',"model":"mustang","year":"1964"}
print("dictionary",mycar)

for x in mycar:
    print (x)#print key
    print (mycar[x])#print value

for x in mycar.keys():
    print (x)#anouther way to print key
for x in mycar.values():
    print (x)#anouther way to print values

for x,y in mycar.items():
    print (x,y)

carinfo=mycar.copy()
print(carinfo)#copy the value of mycar into carinfo

carinfo=dict(mycar)
print(carinfo)# another way of copy the value of mycar into carinfo


mycars={
    "car1" :{
        "name":"fordmustung",
        "year":"1964"
        },
    "car2" :{
        "name":"tesla cybertruck",
        "year":"2023"
        }
    }
print(mycars)
print(mycars["car1"]["name"])
