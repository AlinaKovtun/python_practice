year = int(input('Year: '))
if (not year % 4 and year % 100) or not year % 400:
    print(year, ' is a leap year.')
else:
    print(year, ' is not a leap year.')