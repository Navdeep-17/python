name = str(input("Enter your name:"))
age = int(input("Enter your age"))
gender = str(input("Enter your gender:"))
print(" Name :",name)
print("Age  :",age)
print("gender :",gender)
if(age>18):
        if(gender==male):
             print("you are eligible to vote ")
        else:
             print("you are eligible to vote young lady")
elif(age==18):
    print("Next year you can eligile to vote")
else:
    print("Not eligible to vote")
