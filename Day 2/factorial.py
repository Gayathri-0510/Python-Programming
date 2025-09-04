def factorial(n):
    res=1
    while(n>1):
        res*=n
        print(n,end='*')
        n-=1
    print('1')
    print("\n",res)
factorial(5)