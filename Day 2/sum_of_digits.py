def sumOfDigits(n):
    sum=0
    while n>=1:
        sum+=n%10
        n//=10
    print(sum)
sumOfDigits(123)
sumOfDigits(54321)