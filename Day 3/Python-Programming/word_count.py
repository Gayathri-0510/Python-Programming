def wordCount():
    s='Hi hello how are you'
    spl=s.split()
    cnt=0
    for w in spl:
        cnt+=1
    print(s)
    print("Number of words in string : ",cnt)
wordCount()