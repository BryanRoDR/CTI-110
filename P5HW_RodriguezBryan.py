# Making multiple functions
# 10/11/23
# CTI-110 P5HW - Math Quiz
# Bryan Rodriguez Rosa

#Create Function
def adding(num1, num2):
    result = num1 + num2
    return result

def subtracting(num1, num2):
    result = num1 - num2
    return result
#Main Function
def main():
    user_choice = 0


    while user_choice != 3:
        print("Welcome to the Main Menu")
        print("------------------------")
        print("1.Addition")
        print("2.Subtraction")
        print("3.End Program")

        user_choice = int(input("Enter your Choice: "))

        if user_choice == 1:
            num1 = int(input("Enter your Input: "))
            num2 = int(input("Enter another Input: "))
            print(adding(num1, num2))
            user_choice = int(input("Enter your Choice: "))
            
        if user_choice == 2:
            num1 = int(input("Enter your Input: "))
            num2 = int(input("Enter another Input: "))
            print(subtracting(num1, num2))
            user_choice = int(input("Enter your Choice: "))
            
        if user_choice == 3:
            print("Goodbye")
        else:
            print("You Entered an Invalid Choice")

#Call Main Function
main()

    
