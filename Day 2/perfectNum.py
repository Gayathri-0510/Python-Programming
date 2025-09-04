def perfect(n):
    for i in range(1,n+1):
        total=0
        for j in range(1,i):
            if(i%j == 0):
                total+=j
        if(total==i):
            print(i, end=" ")
perfect(150)