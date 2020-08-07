"""
File name : copyfile.py
Author's name : Noushig Chitjian
Student Number : 301117936
Subject / Description : COMP 301 - Assignment03
file description : This will copy the all the contents of one file into another file

"""

# this will prompt the user to enter the source file name
sourceFile=input("please enter the source filename : ")

# this will prompt the user to enter the destination file name 
destinationFile=input("please enter the destination filename : ")

# this will open the source file in read mode
sourceFile=open(sourceFile,"r")

# this will open the destination file in write mode
destinationFile=open(destinationFile,"w")

# this will read the content of source file and assign it as a content...
textFile=sourceFile.read()

# this will write the content to the destination file...
destinationFile.write(textFile)