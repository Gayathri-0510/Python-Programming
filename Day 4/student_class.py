class Student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
    def display(self):
        print("Name : ",self.name)
        print("Roll No. : ",self.roll_no)
        print("Marks : ",self.marks)

stu1=Student("Ram",503,96)
stu2=Student("Sita",506,89)
stu1.display()
stu2.display()