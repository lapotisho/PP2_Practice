class cat: 
    meow = True
    paws = 4
    def say(self):
        return "meow"
a = cat()
print(a.meow)
print(a.paws)
print(a.say())
del a # this cancels the class attributes and methods inside of a
print(a.meow)