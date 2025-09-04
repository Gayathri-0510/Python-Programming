#Calculate total units and current bill and all customer details
cno=int(input("Enter customer number"))
cname=str(input("Enter customer name"))
pmr=int(input("enter present month reading"))
lmr=int(input("enter last month reading"))
total_units=pmr-lmr
current_bill=total_units*3.80
if 1<total_units<50:
    current_bill=total_units*3.80
elif 51<total_units<100:
    current_bill=(50*3.80)+((total_units-50)*4.20)
elif 100<total_units<200:
    current_bill=(50*3.80)+(50*4.20)+((total_units-100)*5.10)
elif 200<total_units<300:
    current_bill=(50*3.80)+(50*4.20)+(100*5.10)+((total_units-200)*6.30)
else:
    current_bill=(50*3.80)+(50*4.20)+(100*5.10)+(100*6.30)+((total_units-300)*7.50)
    
   
print("Customer number is ", cno)
print("customer name is ", cname)
print("Customer's present month reading is ", pmr)
print("customer's last month reading is ", lmr)
print("total units consumed are", total_units)
print("Current bill is" , current_bill)