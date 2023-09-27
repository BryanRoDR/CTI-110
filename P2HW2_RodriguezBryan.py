#CTI-110
#P2HW2 - List
#Bryan Rodriguez
#9/27/2023

from statistics import mean

module1= float(input("Enter Grade for Module 1: "))
module2= float(input("Enter Grade for Module 2: "))
module3= float(input("Enter Grade for Module 3: "))
module4= float(input("Enter Grade for Module 4: "))
module5= float(input("Enter Grade for Module 5: "))
module6= float(input("Enter Grade for Module 6: "))

#Create an empty list

grades_list = []

grades_list.append(module1)
grades_list.append(module2)
grades_list.append(module3)
grades_list.append(module4)
grades_list.append(module5)
grades_list.append(module6)

print(f'The Lowest grade is: {min(grades_list):.1f}')
print(f'The Highest grade is: {max(grades_list):.1f}')
print(f'The Sum grade is: {sum(grades_list):.1f}')
print(f'The Average grade is: {mean(grades_list):.2f}')
