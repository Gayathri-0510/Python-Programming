def evenOddCount():
    li=[2,0,9,7,4,0,7,6]
    e=0
    o=0
    for i in li:
        if (i%2 == 0):
            e+=1
        else:
            o+=1
    print("Even Count : ",e)
    print("Odd Count : ",o)
evenOddCount()