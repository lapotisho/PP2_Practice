class Employee:
    raise_amount = 1.04
    count = 0
    def __init__(self, name, sname, salary):
        self.name = name
        self.sname = sname
        self.salary = salary
        Employee.count += 1
    def fullname(self):
        return f"{self.name} {self.sname}"
    def apply_raise(self):
        self.salary *= Employee.raise_amount
    @classmethod
    def total_employees(cls):
        return cls.count
emp1 = Employee("Azamat", "Bek", 50000)
emp2 = Employee("Anelya", "Sarsen", 60000)
print(emp1.fullname())       
print(emp1.salary)   
print(emp1.raise_amount) 
emp1.raise_amount=1.05
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.raise_amount)
emp1.apply_raise()
print(emp1.salary)            
print(Employee.total_employees())  
