"""

File name : payroll.py

Author's name : Noushig Chitjian

Student Number : 301117936

file description : This will read the data.txt file and outputs the wages

                   of employees in a nice format to the console

"""
# Task 02
# this will prompt the user to enter the file name
Name = input("please enter the file name : ")

# this will open the file that user input in the console
data = open(Name,"r")

# this will read the texts from the data.txt and assign it as display lists for payroll.py
lists = data.readlines()

# this will print the table headers as shown in print mode
print(" Employee Number |    Employee Name    | Hours Worked ")

# table seperation line for more clarity
print("-----------------------------------------------------")

# table style

