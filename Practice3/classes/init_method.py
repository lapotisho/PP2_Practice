class person: 
    total_people = 0
    def __init__(self,name,surname,age,origin):
        self.name=name
        self.surname=surname
        self.age=age
        self.origin=origin
        person.total_people+=1
    def info(self):
        print(self.name)
        print(self.surname)
        print(self.age)
        print(self.origin)
a = input("Greeting what's your name: ")
b = input("what's your surname: ")
c = int(input("enter your age: "))
d = input("where are you from: ")
person1=person(a,b,c,d)
person1.info()
print("how many people are listed:",end=' ')
print(person.total_people)