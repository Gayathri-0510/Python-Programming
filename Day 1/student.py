#calculate total average marks of student and print all student details
sno=int(input("Enter Student number : "))
sname=str(input("enter student name : "))
sub1,sub2,sub3=map(int,input("Enter 3 sub marks : ").split())
total=(sub1+sub2+sub3)
average=total/3
print("student number : ", sno)
print("student name : " , sname)
print("total marks : " ,total)
print("average marks : " ,round(average,2))