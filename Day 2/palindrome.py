def palindrome(n):
    for i in range(1,n+1):
        n_str=str(i)
        rev=n_str[::-1]
        if(n_str == rev):
            print(n_str,end=" ")
palindrome(150)