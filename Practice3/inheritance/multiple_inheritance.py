class Person: # parent class
    def __init__(self, name): # takes name and writes it
        self.name = name
    def infoo(self): # it'll return it back
        return f"Name: {self.name}"
class Worker: # second parent class
    def __init__(self, salary):# writes the salary 
        self.salary = salary
    def infa(self): # output it
        return f"Salary: {self.salary}"
class Employee(Person, Worker): # multiple inheritance or child class
    def __init__(self, name, salary):
        Person.__init__(self, name) # now it creates an object of Person inside of this function
        Worker.__init__(self, salary)
    def info(self):
        return f"{Person.infoo(self)}, {Worker.infa(self)}"
e = Employee("Azamat", 50000)
print(e.info()) 