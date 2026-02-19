class Person: # parent class
    def __str__(self):
        return "Hello, I am a person"
class Employee(Person): #child class
    def __str__(self): 
        return "Hello, I am an employee" # class's own implications which affects only this class objects
a = Person()
b = Employee()
print(a)
print(b)
class Animal:
    def eat(self):
        print("this Animal is eating")
class Rabbit(Animal):
    def eat(self):
        print("this Rabbit is eating carrots")
a = Animal()
a.eat()
del a
a = Rabbit()
a.eat()