number_of_subject=int(input("enter number of subject:"))
a=[]
print ("Enter your mark")
for i in range (number_of_subject):
  num=int(input("Enter " +str(i+1)+ " subject mark :"))
  a.append(num)
print (a)
sum=0

for i in a:
    sum=sum+i
print("Sum :" , sum)
print("Avg :",sum/number_of_subject)
