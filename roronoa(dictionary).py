mycar ={"brand":'ford',"model":"mustang","year":"1964"}
print("dictionary",mycar)

mycar ={"brand":'ford',"model":"mustang","year":"1964","year":"2020"}#overwriting
print("dictionary",mycar)
print("number of item in dictionary :",len(mycar))

mycar =dict(brand='ford',model="mustang",year="1964")#another way to make dict
print("another way to make dictionary",mycar)


print("\n")

print(mycar["model"])

print(mycar.get("model"))#anouther way

print(mycar.keys())

print(mycar.values())
mycar["color"]="black"
print(mycar)
mycar["year"]="2025"
print(mycar)

z= mycar.items()
print("return each item as the tuple in list:",z)

if 'model' in mycar :#member ship
    print("check if model in dict or not:","yes 'model' is one of the key in dictionary")
    
    
print("\n")


mycar.pop("year")
print(mycar)
del mycar["color"]
print(mycar)
mycar.clear()
print(mycar)


d1={"a": 1, "b": 2}#fetching
d2 = {"c": 3}
d3=d1 | d2
print(d3)
d2.update({"b": 5, "e": 6})
print(d2)
d2 = d.copy()
print(d3)



