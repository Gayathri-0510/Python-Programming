def primeFactors(n):
    for i in range(2,n):
        if n%i==0:
            for j in range (2,i):
                if i%j==0:
                    break
            else:
                print(i, end=" ")
primeFactors(15)