def armstrong(n):
    for i in range(1,n+1):
        n_str=str(i)
        l=len(n_str)
        total=0
        for d in n_str:
            total +=int(d)**l
            if total == i:
                print(i, end=" ")
armstrong(153)