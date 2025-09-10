def unique():
    li=[1,1,4,9,2,7,9]
    uniqueList=[]
    i=0
    li.sort()
    n=len(li)
    while i<n:
        cnt=1
        j=i
        while j<n-1 and li[j]==li[j+1]:
            cnt+=1
            j+=1
        if(cnt==1):
            uniqueList.append(li[i])
        i=j+1
    print(uniqueList)
unique()