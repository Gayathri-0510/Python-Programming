def cntOccurance():
    s='gayathri'
    a='a'
    cnt=0
    for i in range (len(s)):
        if(s[i]==a):
            cnt+=1
    print("'a' occurs ",cnt,"times in a string")
cntOccurance()