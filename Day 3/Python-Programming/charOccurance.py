def charOcurence():
    s='hi hello'
    m='h'
    positions=[]
    for i in range(len(s)):
        if (s[i]==m):
            positions.append(i)
    print("Occourance of 'h' in string is ",positions)
charOcurence()



