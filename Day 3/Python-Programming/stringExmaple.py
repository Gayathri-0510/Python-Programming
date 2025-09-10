def string():
    s='gayathri'
    res=''
    s=sorted(s)
    i=0
    while i<len(s):
        j=i
        cnt=1
        while j<len(s)-1 and s[j]==s[j+1]:
            cnt+=1
            j+=1
        res+=s[i]+str(cnt)
        i=j+1
    print(res)
string()
        