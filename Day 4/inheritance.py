class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def display(self):
        print("Employee Name : ",self.name)
        print("Employee salary : ",self.salary)
class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department=department
    def display(self):
        super().display()
        print("Department : ",self.department)
emp1=Employee("Sai",80000)
mang1=Manager("Ram",100000,"HR")
emp1.display()
mang1.display()
    