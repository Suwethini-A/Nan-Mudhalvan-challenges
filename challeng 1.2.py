#Get input from user
year=int(input("Enter a Year : "))
#check if it's a leap year 
if( ( year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0 )):
  print(f"\n{year} is a leap year.")
else:
  print(f"\n{year} is not a leap year.")
