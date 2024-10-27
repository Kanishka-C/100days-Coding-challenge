month,year=map(int,(input('Enter the month and year : ').split()))
if month==2 and (year%400==0 or year%100!=0 and year%4==0):
    print(29)
elif month==2:
    print(28)
elif month in (1,3,5,7,8,10,12):
    print(31)
else:
    print(30)