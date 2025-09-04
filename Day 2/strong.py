def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def strong(n):
    for i in range (1,n+1):
        total=0
        for d in str(i):
            total+=fact(int(d))
        if i==total:
            print(i,end=" ")
strong(150)