def pattern(r,c):
    for i in range(r):
        for j in range (c):
            if (i==j) or (i==(c-j-1)):
                
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
pattern(5,5)