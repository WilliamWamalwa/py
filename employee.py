class Employee :
    def __init__(self,name,position,salary):
        self.name=name
        self.position=position
        self.salary=salary

    def info(self):
        print(self.position,"is earning",self.salary)

employee1= Employee("John","CEO",200000)
print(employee1.name,employee1.position,employee1.salary)
employee2= Employee("John","CEO",200000)
employee3= Employee("John","CEO",200000)
employee4= Employee("John","CEO",200000)
employee5= Employee("John","CEO",200000)