class Person: 
    def __init__(self,name,surname,age): # initial function
        self.name = name
        self.surname = surname
        self.age = age
    def info(self): 
            print(f"The full name of a student {self.name} {self.surname} age: {self.age}")
class student(Person):
    count = 0
    def __init__(self,name,surname,age,grade,gpa):
        super().__init__(name,surname,age) # uses the function from the parent class
        self.grade = grade 
        self.gpa = gpa
        student.count+=1
    def stats(self): 
        print(f"the grade is {self.grade} and gpa {self.gpa}")
class teacher(Person): 
    def __init__(self,name,surname,age,subject):
        super().__init__(name,surname,age)
        self.subject=subject
    def info(self): # overrides the parent's class function
        print(f"The full name of a student {self.name} {self.surname} age: {self.age}, subject: {self.subject}")
student1 = student("Artem","Brainstor",15,9,2.9)
student1.info()
student1.stats()
teacher1 = teacher("Nurlan","Kadyrov",30,"Physics")
teacher1.info()