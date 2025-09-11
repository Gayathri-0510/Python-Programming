#check if a year is leap year or not
def leap(y):
    if (y%100!=0 and y%4==0) or (y%100==0 and y%4==0 and y%400==0):
        print(y,"is a leap year")
    else:
        print(y,"is not a leap year")
leap(1940)
leap(2000)
leap(2025)
leap(2020)