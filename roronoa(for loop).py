a = int(input("Enter tne number:"))
b = int(input("Enter tne number:"))
even_count=0
odd_count=0
for i in range(a,b):
    if(i%2==0):
        even_count=even_count + 1  
    else:
        odd_count=odd_count+1
    print("Even_count:",even_count)
    print("Odd_count:",odd_count)
    #above to print statements print every itration beause it is inside a loop
print("Even_count:",even_count)
print("Odd_count:",odd_count)#here print only final count


fruits =["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x== "banana":
     break #break affter print

fruits =["apple","banana","cherry"]
for x in fruits:
    if x== "banana":
     break
    print(x)#break before print


fruits =["apple","banana","cherry"]
for x in fruits:
    if x== "banana":
     continue # it stop currunt iteration and move to next iteration
    print(x)


list1 = ["1","2","3"]
list2 = ["1","2","3"]
for x in list1:
 for y in list2:
     print(x,y)
