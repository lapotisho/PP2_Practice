class cat: 
    meow = True
    paws = 4
    def say(self):
        return "meow"
a = cat()
print(a.meow)
print(a.paws)
print(a.say())
class kinda_cat(cat): # it takes the properties of the class in this case class cat
    pass
x = kinda_cat()
print(x.meow)
print(x.paws)
print(x.say())