def setEx(n):
    s.add(n)
s=set()
n=int(input("Enter number of elements:"))
for i in range (n):
    inp=int(input("Enter element"))
    setEx(inp)
print(s)
