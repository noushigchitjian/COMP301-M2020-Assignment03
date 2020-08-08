"""

File name : payroll.py

Author's name : Noushig Chitjian

Student Number : 301117936

Subject / description : COMP 301 - Assignment03

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

# this will split the display by comma and assigns it in the employeeInf to display it in a nice format
for display in lists:
    employeeInf = display.split(",")    
    employeeNum = employeeInf[0]
    employeeName = employeeInf[1]+" "+ employeeInf[2]
    hoursWorked = employeeInf[3]
    
    # this will print the data in a required format...
    print("   %10s    |%20s | %7s " %(employeeNum,employeeName,hoursWorked))


    

