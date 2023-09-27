#First Last
#9/27/2023
#Use float number in calculation

mpg = float(input("Enter Miles Per Gallon: "))
gasmoney = float(input("Enter Cost Per Gallon: "))
cost_20 = (20/mpg)*gasmoney
cost_75 = (75/mpg)*gasmoney
cost_500 = (500/mpg)*gasmoney

print(f"The cost to drive 20 miles is {cost_20:.2f}")
print(f"The cost to drive 75 miles is {cost_75:.2f}")
print(f"The cost to drive 500 miles is {cost_500:.2f}")
