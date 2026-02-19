class Students:
    cnt=0
    total_gpa=0
    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Students.cnt+=1 # every time we add new student the function activates then our attribute cnt adds 1 element
        Students.total_gpa+=gpa
    @classmethod
    def avg_gpa(cls):
        if cls.cnt == 0: 
            return 0
        else: 
            return cls.total_gpa/cls.cnt
student1 = Students("Azamat",3.3)
student2 = Students("Anelya",4.0)
print(student1.name,student1.gpa)
print(student1.name,student2.gpa)
print(Students.cnt)
print(Students.avg_gpa())
class Circle():
    def __init__(self,r):
        self.r=r
    def area():
        return 3.14 * self.r ** 2
class Square():
    def __init__(self,a):
        self.a=a
    def area(self):
        return self.a**2
class Triangle():
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return self.base * self.height/2
c=[Circle(5),Triangle(6,7),Square(5)]
for x in c :
    print(x.area())