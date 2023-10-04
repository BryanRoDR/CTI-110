#Intro to Loops using the range function
#Bryan Rodriguez
#10/4/23

num1 = int(input("Enter A Number: "))
num2 = int(input("Enter A Number: "))

#First num is smaller
if num1 <= num2:
    #Execute for loop using range(start,stop,increment)
    for x in range(num1, num2+1, 5):
        print(x)

else:
    print("The First Number must be SMALLER. ")
