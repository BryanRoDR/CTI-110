#Bryan Rodriguez Rosa
#10/2/2023
#This is using IF statements to determine Leap Year

#get input from user

   
input_year = int(input("Enter a Year: "))
if input_year % 4 == 0:
    if input_year % 100 == 0:
        if input_year % 400 == 0:
            print("The year is a leap year")

        else:
            print("The year is NOT a leap year")
    else:
        print("The year is NOT a leap year")
else:
    print("The year is NOT a leap year")

                
        
