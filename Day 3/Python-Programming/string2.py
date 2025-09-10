def findCNT():
    s='123str@#$'
    alpha=0
    dig=0
    spl=0
    for char in s:
        if char.isalpha():
            alpha+=1
        elif char.isdigit():
            dig+=1
        else:
            spl+=1
    print("No. of alphabets : ",alpha)
    print("No. of digits : ",dig)
    print("No. of special characters : ",spl)
findCNT()