myfile = open("myfile.txt")
content = myfile.read()
print(content)
myfile.seek(0) #reset the cursor in the beginning
print(myfile.readlines())

myfile.close() #to close the opening file

#or
with open("myfile.txt", mode="r") as myfile:
    content = myfile.read()
print(content)

#writing on a file
with open("myfile.txt", mode="a") as writefile:
    writefile.write('\nfour in fourth')

with open("myfile.txt", mode="r") as myfile:
    content = myfile.read()
print(content)

#created a file
with open("newFile.txt", mode="w") as newfile:
    newfile.write("this is a new created file")
with open("newFile.txt", mode="r") as myfile:
    content = myfile.read()
print(content)
