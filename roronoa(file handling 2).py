with open("C:\\Users\\NAVDEEP\\OneDrive\\Desktop\\pty.txt","w+") as f:
#with no need to close the file
#"as f" mean f= open(".....")
    lst=["navdeep \n","dinesh \n","harish \n"]
    f.writelines(lst)#write a multiple string
    f.seek(0)#move pointer back to start ,if "6"insted"0" start from "p"
    print(f.readlines())#read a file line by line and return as a list of string
    a=str(f)
    print(type (a))
    b=f.tell()#give current pointer position
    print("position",b)
    f.seek(0)
    f.read(5)
    print(f.tell())
