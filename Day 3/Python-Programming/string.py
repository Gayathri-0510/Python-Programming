def lenStr():
    s1="Hello"
    s2="Hi"
    cnt1=0
    cnt2=0
    for char in s1:
        cnt1+=1
    for char in s2:
        cnt2+=1
    print("Length of s1 : ",cnt1)
    print("Length of s2 : ",cnt2)
    if(s1 ==s2):
        print ("Equal")
    else:
        print("Not equal")
    print(s1+s2)
lenStr()