#Rodriguez Rosa Bryan
#10/11/23
#CTI-110
#Playing with functions

def leap_year_calc(input_year):
    
    is_leap_year = False

    if (input_year % 4) == 0:      # inputYear is divisible by 4
      if (input_year % 100) == 0:   # inputYear is divisible by 100 (century year)
        if (input_year % 400) == 0: # inputYear is divisible by 400
          is_leap_year = True
        else:           # inputYear is not divisible by 400
          is_leap_year = False
      else:             # inputYear is not divisible by 100
        is_leap_year = True
    else:               # inputYear is not divisible by 4
      is_leap_year = False
    if is_leap_year:
        return True
    else:
        return False


#Main Function Starts Here

def main():
    input_year = int(input("Enter a Year: "))
    result = leap_year_calc(input_year)
    if result == True:
        print(f"{input_year} is a leap year")
    else:
        print(f"{input_year} is a NOT leap year")

#Call the main function
main()
