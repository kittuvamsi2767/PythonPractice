#2. Write program to write or create file from python?
'''
# Create a file using python program
f = open('inputfile1.txt','x')
'''
# Code to delete the existing file and create new file
import os
file1 = input("Enter input file Name: ")
if os.path.exists(file1):
    os.remove(file1)
    f = open(file1,'x')
    f.write("Hareesh is working on Python program")
    f.close()
else:
    print(file1 + " File doesnot exists, so created the file")
    f = open(file1,'x')
    f.write("Hareesh is working on Python program")
    f.close()
f = open(file1,'r')
print(f.read())

