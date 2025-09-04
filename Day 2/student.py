sno=int(input("Enter student number"))
sname=str(input("Enter student name"))
sub1, sub2, sub3=map(int,input("Enter 3 subject marks").split())
total=(sub1+sub2+sub3)
average=total/3
if average>=40:
    print("pass")
    if average<50:
        print('C grade')
    elif 51<average<70:
        print('B grade')
    elif 71<average<80:
        print('C grade')
    else:
        print('Distension')
else:
    print('Fail')