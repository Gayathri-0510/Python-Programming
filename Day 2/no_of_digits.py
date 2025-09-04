def noOfDigits(n):
    cnt=0
    while n>=1:
        cnt+=1
        n//=10
    print(cnt)
noOfDigits(123)
noOfDigits(54321)