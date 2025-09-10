def frequency():
    li=[0,9,7,7,5,8,8]
    n=len(li)
    li.sort()
    i=0
    while i<n:
        j=i
        cnt=1
        while j<n-1 and li[j] == li[j+1] :
            cnt+=1
            j+=1
        print(li[i]," -> ",cnt)
        i=j+1
frequency()