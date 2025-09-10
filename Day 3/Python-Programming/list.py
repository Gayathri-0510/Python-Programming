def list1(n):
    li.append(n)
li=[]
a=int(input("Enter number of elements in list : "))
for i in range (a):
    inp=int(input("Enter input : "))
    list1(inp)
print(li)