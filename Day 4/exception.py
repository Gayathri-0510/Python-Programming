def exception():
    n=int(input("Enter numerator : "))
    d=int(input("Enter denominator : "))
    try:
        res=n/d
        print("Result : ",res)
    except:
        print("Denominator can't be zero")
exception()