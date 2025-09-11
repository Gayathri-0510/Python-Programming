#convert days to years and months
def conversion(d):
    years=d//365
    months=d//30
    print("Years : ",years)
    print("Months : ",months)
d=int(input("Enter number of days : "))
conversion(d)