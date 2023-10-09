# CTI-110
# P3HW2 - Salary
# Bryan Rodriguez Rosa
# 10/4/23
# If Else statements to determine gross payments

name = ""

count = 0
total_pay = 0

while name != "Done":
# get input from user
    name = input("Enter Employee Name: ")
    if name != "Done":
        count = count + 1
        num_hours = float(input("Enter Number of Hours Worked: "))
        pay_rate = float(input("Enter Hourly pay rate: "))
        OT_hours = 0
        has_OT = False
        OT_pay = 0

#Calculate Overtime = yes/no - how much
        if num_hours > 40:
            has_OT = True
            OT_hours = num_hours - 40
        else:
            has_OT = False
        
        if has_OT == True:
            OT_pay = (pay_rate * 1.5) * (num_hours - 40) #Actual OT total pay 
        else:
            OT_pay = 0 

#Calculate regular pay
        reg_pay = pay_rate * (num_hours - OT_hours)
        gross_pay = reg_pay + OT_pay
        total_pay = total_pay + gross_pay

#Display name, pay rate, num hours worked, OT Hours OT pay, gross pay

        print("Name: ", name)
        print("Overtime hours: ", OT_hours)
        print("Overtime Pay: ", OT_pay)
        print("Regular Hours: ", num_hours - OT_hours)
        print("Regular Pay: ", reg_pay)
        print("Gross Pay Rate: ", reg_pay + OT_pay)
#While Loop Breaks
print("Total amount of Employees entered:", count)
print("Total paid to Employees:", total_pay)

