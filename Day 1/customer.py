def customer():
    cno=int(input("Enter customer number : "))
    cname=str(input("Enter customer name : "))
    pmr=int(input("enter present month reading : "))
    lmr=int(input("enter last month reading : "))
    total_units=pmr-lmr
    current_bill=total_units*3.80
    print("Customer number is ", cno)
    print("customer name is ", cname)
    print("Customer's present month reading is ", pmr)
    print("customer's last month reading is ", lmr)
    print("total units consumed are", total_units)
    print("Current bill is" , current_bill)
customer()