#kilometer to miles
def km_to_miles(km):
    miles=km*0.621371
    return miles
n=int(input("Enter kilometers : "))
print(n," kilometers = ",km_to_miles(n)," miles")