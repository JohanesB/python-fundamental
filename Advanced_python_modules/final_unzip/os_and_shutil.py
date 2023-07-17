# f = open("practice.txt", "w+")
# f.write("This is a test string")
# f.close()

import os
print(os.getcwd())
print(os.listdir('C:\\Users\\Yohanes\\Desktop\\dev\\python'))

import shutil
# print(shutil.move("practice.txt", 'C:\\Users\\Yohanes\\Desktop\\dev\\python'))
# print(shutil.move('C:\\Users\\Yohanes\\Desktop\\dev\\python\\practice.txt', os.getcwd()))


for folder, subfolders, files in os.walk("C:\\Users\\Yohanes\\Desktop\\dev\\python"):
    print(f'Currently looking at {folder}')
    print("\n")

    print("The subfolders are: ")
    for subfolder in subfolders:
        print(f"\t Subfolder: {subfolder}")

    print("\n")
    print("The files are: ")
    for file in files:
        print(f"\t File: {file}")
    print("\n")
