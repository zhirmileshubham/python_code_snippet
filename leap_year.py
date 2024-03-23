'''
Below code check if given year is a leap year or not...
'''

def leap_year(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
year = int(input('Enter the year to check if it is leap year or not :'))

if leap_year(year):
    print("Given year is a leap year")
else:
    print("Given year is not a leap year")
