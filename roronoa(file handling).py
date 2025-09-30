f=open("C:\\Users\\NAVDEEP\\OneDrive\\Desktop\\pty.txt","w")
f.write("Yoko So Watha Shino Python File Handling")#write a single string
print("File name : ",f.name)#return file name
print("Mode :",f.mode)#return mode
print(f.writable())#check file is writable or not
f.seek(0)
print(f.read(0))
print(f.closed)#check file is closed or not
f.close()
print(f.closed)