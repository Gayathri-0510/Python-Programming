#find simple interest and total amount
p=int(input("Enter principle amount"))
r=int(input("enter rate of interest"))
t=int(input("enter total number of months"))
si=(p*t*r)/100
amt=p+si
print("simple interest",si)
print("total amount",amt)