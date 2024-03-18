print("CALCULATE LEAP YEAR")

year=int(input("Enter the year :"))


if((year % 400 == 0) or  
     (year % 100 != 0) and  
     (year % 4 == 0)):
    print("Given Year is a leap Year")
else:
    print("given year is not a leap year")
    while year!=100000000000:
        year=int(input("Enter the year :"))

